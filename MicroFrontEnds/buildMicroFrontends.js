const fs = require("fs");
const path = require("path");
const child_procsss = require("child_process")

// This function accept the current path and run npm install in all the Microfontends
function buildMicroforntEnds(current_path, commad_to_run){
    const subDirs = fs.readdirSync(current_path).filter(
        (item)=>fs.statSync(path.join(current_path, item)).isDirectory()
    );
    subDirs.forEach((dir)=>{
        if(fs.existsSync(path.join(dir, 'package.json'))){
            console.log("=====Installng NPM requirements in MicrofrontEnd====" + structuredClone(dir))
            child_procsss.execSync(commad_to_run, {cwd: dir})
        }
    })
}


const current_path = path.resolve(process.cwd())
const commad_to_build = "npm install --force"
buildMicroforntEnds(current_path, commad_to_build)