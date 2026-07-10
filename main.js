const {app, BrowserWindow}=require('electron');
app.whenReady().then(()=>{
    const win=new BrowserWindow({
        width:500,
        height:600,
        webPreferences:{nodeIntegration:true,contexIsolation:false}

    });
    win.loadFile('scanner.html');
});