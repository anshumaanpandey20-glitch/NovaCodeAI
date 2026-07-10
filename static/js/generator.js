// =========================
// Copy Code
// =========================

const copyBtn = document.getElementById("copyBtn");

if (copyBtn) {

    copyBtn.addEventListener("click", () => {

        const code = document.getElementById("generatedCode").innerText;

        navigator.clipboard.writeText(code);

        copyBtn.innerHTML = "Copied";

        setTimeout(() => {

            copyBtn.innerHTML = "Copy Code";

        }, 2000);

    });

}



// =========================
// Download Code
// =========================

const downloadBtn = document.getElementById("downloadBtn");

if (downloadBtn) {
    downloadBtn.addEventListener("click", () => {
        const code = document.getElementById("generatedCode").innerText;
        const language = document
            .getElementById("selectedLanguage")
            .value
            .toLowerCase();
        let extension = "txt";
        switch (language) {
            case "python":
                extension = "py";
                break;
            case "javascript":
                extension = "js";
                break;
            case "java":
                extension = "java";
                break;
            case "c++":
                extension = "cpp";
                break;
            case "c":
                extension = "c";
                break;
            case "html":
                extension = "html";
                break;
            case "css":
                extension = "css";
                break;
            case "sql":
                extension = "sql";
                break;
            default:
                extension = "txt";
        }
        const blob = new Blob([code], {
            type: "text/plain"
        });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `generated_code.${extension}`;
        a.click();
        URL.revokeObjectURL(url);
    });
}
// Highlight generated code
if (typeof Prism !== "undefined") {
    Prism.highlightAll();
}
const form = document.querySelector("form");

const loader = document.getElementById("loader");

const generateBtn = document.getElementById("generateBtn");

if(form){

    form.addEventListener("submit", function(){

        loader.style.display = "block";

        generateBtn.disabled = true;

        generateBtn.innerHTML = "Generating...";

    });

}
