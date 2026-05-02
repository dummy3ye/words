const { exec } = require('child_process');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const menu = () => {
    console.log('\n--- WORDS HARVESTER COMMAND CENTER ---');
    console.log('1. [RUN] Full Pipeline (Sync -> Scrape -> Clean -> Parse)');
    console.log('2. [SYNC] Sync new URLs only');
    console.log('3. [SCRAPE] Fetch fresh data');
    console.log('4. [QUIT] Exit');
    
    rl.question('\nSelect an option: ', (choice) => {
        switch(choice) {
            case '1': execute('python run.py'); break;
            case '2': execute('node src/urls.js'); break;
            case '3': execute('python src/main.py'); break;
            case '4': rl.close(); process.exit();
            default: console.log('Invalid choice.'); menu();
        }
    });
};

const execute = (cmd) => {
    console.log(`\n> Executing: ${cmd}...`);
    exec(cmd, (err, stdout, stderr) => {
        if (err) console.error(`Error: ${err.message}`);
        if (stdout) console.log(stdout);
        menu();
    });
};

menu();
