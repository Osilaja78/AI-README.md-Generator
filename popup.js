
document.addEventListener("DOMContentLoaded", function () {
    const generateButton = document.getElementById("generateButton");
    generateButton.addEventListener("click", generateReadme);
});

async function generateReadme(e) {
    e.preventDefault();

    const repoName = document.getElementById("repoName").value;
    const repoDescription = document.getElementById("repoDescription").value;

    try {
        const response = await fetch("https://readmegenerator-1-x0178516.deta.app/ask_gpt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            repoName: repoName,
            repoDescription: repoDescription
        }),
        });

        const data = await response.json();
        const aiGeneratedContent = data.response ? data.response : null;

        if (aiGeneratedContent !== null)  {
            const blob = new Blob([aiGeneratedContent], { type: "text/plain;charset=utf-8" });
            const filename = "README.md";

            const downloadLink = document.createElement("a");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = filename;
            downloadLink.click();
        } else {
            console.error("An error occured...");
        }
    } catch (error) {
        console.error("Error generating README:", error);
    }
}
