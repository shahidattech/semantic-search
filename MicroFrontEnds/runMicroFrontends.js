const fs = require("fs");
const path = require("path");
const child_procsss = require("child_process");
const { rejects } = require("assert");

// Run Microfrontends based on it's Package.json defination
function runMicroforntEnds(current_path){
    
    const subDirs = fs.readdirSync(current_path).filter(
        (item)=>fs.statSync(path.join(current_path, item)).isDirectory()
    );
    
    const asyncProcessCommand = subDirs.map((dir)=>{
        if(fs.existsSync(path.join(current_path, dir), 'package.json')){
            console.log("====Starting Application=====" + structuredClone(dir))
            const asyncProcess = child_procsss.spawn('npm', ['start'], {cwd: dir, shell: true});
            return new Promise((resolve, reject) =>{
                asyncProcess.stdout.on('data', (data)=>{
                    console.log(`====Async Process O/P  in === ${dir} ${data}`)
                });
                asyncProcess.stderr.on('data', (data)=>{
                    console.log(`====Async Process Error=== in ${dir} Error ${data}`);
                });
                asyncProcess.on('close', (code)=>{
                    if (code==0){
                        console.log(`====Async Process Completed Successfully for for ${dir}`);
                        resolve();
                    }
                    else{
                        console.log(`====Async Process Failed due to ${code} in ${dir}`);
                        reject();
                    }
                });
            });
        }
    });

    Promise.all(asyncProcessCommand).then(()=>{
        console.log("=====Async process Completed Successfully====")
    }).catch(()=>{
        console.log("Async Process Got an Error====")
    })
}

const current_path = path.resolve(process.cwd())
runMicroforntEnds(current_path)