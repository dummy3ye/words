const fs = require('fs');
const path = require('path');

// Paths relative to project root
const TXT_FILE = path.join(__dirname, '..', 'urls.txt');
const JSON_FILE = path.join(__dirname, '..', 'urls.json');

function syncUrls() {
    try {
        const txtContent = fs.readFileSync(TXT_FILE, 'utf8');
        const urls = txtContent.split('\n').map(line => line.trim()).filter(line => line.length > 0);

        let jsonData = [];
        if (fs.existsSync(JSON_FILE)) {
            jsonData = JSON.parse(fs.readFileSync(JSON_FILE, 'utf8'));
        }

        const existingUrls = jsonData.map(entry => entry.url);
        let addedCount = 0;

        urls.forEach(url => {
            if (!existingUrls.includes(url)) {
                jsonData.push({
                    url: url,
                    scraped: false,
                    last_scraped: null,
                    tokens_count: 0
                });
                addedCount++;
            }
        });

        fs.writeFileSync(JSON_FILE, JSON.stringify(jsonData, null, 2));
        console.log(`[+] Synced: ${addedCount} new URLs added to urls.json.`);

    } catch (err) {
        console.error(`[!] Sync failed: ${err.message}`);
    }
}

syncUrls();
