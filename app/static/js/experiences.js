console.log('This is an test log !');
document.addEventListener('DOMContentLoaded', function() {
// Initialize syntax highlighting
hljs.highlightAll();
 
// Initialize CodeMirror for code cells
document.querySelectorAll('.jp-InputArea-editor').forEach(editor => {
    CodeMirror.fromTextArea(editor, {
        mode: 'python',
        theme: 'default',
        lineNumbers: true,
        readOnly: true
    });
});
});
 
function runAll() {
// This is a placeholder - actual implementation would require backend integration
alert('Running all cells... (This is a demo)');
}
 
function clearOutputs() {
document.querySelectorAll('.jp-OutputArea').forEach(output => {
    output.style.display = 'none';
});
}
 
function downloadNotebook() {
// Create a link to download the notebook
const link = document.createElement('a');
link.href = '/download-notebook';  // You'll need to create this route
link.download = 'experience_center.ipynb';
document.body.appendChild(link);
link.click();
document.body.removeChild(link);
}
 