const { app, BrowserWindow } = require('electron')

/* Start the Flask (app.exe) in the background as a child. */
const { execFile } = require('child_process');
const child = execFile(
    "./aws/dist/app.exe", [],
    {
        windowsHide: false,
        stdio: ["pipe", "pipe", "pipe"],
    }
);

/* Log the Flask stdout and stderr to the console. */
child.stdout.on("data", (data) => {
    console.log(`stdout: ${data}`);
});
child.stderr.on("data", (data) => {
    console.log(`stderr: ${data}`);
});

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    })
    win.loadFile('templates/index.html')
}

app.whenReady().then(() => {
    createWindow();
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        const { exec } = require('child_process');
        exec('taskkill /f /t /im app.exe', (err, stdout, stderr) => {
            if (err) {
                console.log(err)
                return;
            }
            console.log(`stdout: ${stdout}`);
            console.log(`stderr: ${stderr}`);
        });
        console.log('Closing app & child processes.');
        app.quit();
    }
})