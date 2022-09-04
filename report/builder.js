const path = require('path');
const fs = require('fs');

const BaseDir = __dirname
function build(){
  const html = fs.readFileSync(path.join(BaseDir,'report.html'),'utf-8');
  const recordData = fs.readFileSync(path.join(BaseDir,'record.js'),'utf-8');
  const output = html.replace(`<script src="record.js"></script>`,
  `<script>${recordData}</script>`)
  const outputDir = path.join(BaseDir, 'output');
  if(!fs.existsSync(outputDir)){
    fs.mkdirSync(outputDir);
  }
  fs.writeFileSync(path.join(BaseDir, 'output/reporter.html'),output)
}

build()