export default async function handler(req, res) {
    // We accepteren alleen "POST" verzoeken (data versturen)
    if (req.method !== 'POST') {
        return res.status(405).json({ message: 'Method Not Allowed' });
    }

    const { websiteUrl, email, language } = req.body;

    // Haal alle API keys veilig uit Vercel (wordt nooit blootgesteld aan bezoekers!)
    const apiKey = process.env.MINDSTUDIO_API_KEY;
    const agentId = process.env.MINDSTUDIO_AGENT_ID;
    const supabaseUrl = process.env.SUPABASE_URL;
    const supabaseKey = process.env.SUPABASE_ANON_KEY;

    if (!apiKey || !agentId || !supabaseUrl || !supabaseKey) {
        return res.status(500).json({ error: 'Niet alle API Keys staan in Vercel (MindStudio of Supabase ontbreekt).' });
    }

    try {
        // 1. Start de Analyse in MindStudio!
        const msResponse = await fetch('https://v1.mindstudio-api.com/developer/v2/agents/run', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                agentId: agentId,
                workflow: 'Main',
                variables: {
                    websiteContent: '',
                    websiteUrl: websiteUrl,
                    email: email,
                    language: language || 'nl'
                }
            })
        });

        if (!msResponse.ok) {
            const errorText = await msResponse.text();
            return res.status(msResponse.status).json({ error: 'Fout bij MindStudio Cloud', details: errorText });
        }

        // MindStudio heeft geantwoord! We pakken de uitkomst.
        const msData = await msResponse.json();

        // Omdat we in theorie nog niet weten exact welk woordje MindStudio gebruikt voor de output, 
        // slaan we voor de zekerheid het hele resultaat op als tekst:
        const agentOutput = typeof msData === 'object' ? JSON.stringify(msData) : msData;

        // 2. We mikken de Klant, Gegevens én Output succesvol in jouw Supabase Database
        const supabaseEndpoint = `${supabaseUrl}/rest/v1/scan_requests`;

        const sbResponse = await fetch(supabaseEndpoint, {
            method: 'POST',
            headers: {
                'apikey': supabaseKey,
                'Authorization': `Bearer ${supabaseKey}`,
                'Content-Type': 'application/json',
                'Prefer': 'return=minimal' // We hoeven de data niet wéér terug te krijgen van Supabase
            },
            body: JSON.stringify({
                website_url: websiteUrl,
                email: email,
                agent_output: agentOutput
            })
        });

        if (!sbResponse.ok) {
            // Zelfs als Supabase héél even weigert sluiten we de site niet af voor de klant, maar loggen we de fout in Vercel.
            const sbError = await sbResponse.text();
            console.error("Supabase kon de data niet opslaan. Foutmelding:", sbError);
        }

        // 3. Stuur een groen vinkje + de MindStudio uitkomst terug naar het scherm van de klant op brandingmusthaves.com!
        return res.status(200).json(msData);

    } catch (error) {
        console.error("Crash in Serverless Function:", error.message);
        return res.status(500).json({ error: error.message });
    }
}
