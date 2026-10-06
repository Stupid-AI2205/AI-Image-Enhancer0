const dropZone = document.getElementById("dropZone");

const fileInput = document.getElementById("fileInput");

const previewSection =
    document.getElementById("previewSection");

const actionSection =
    document.getElementById("actionSection");

const downloadSection =
    document.getElementById("downloadSection");

const originalImage =
    document.getElementById("originalImage");

const enhancedImage =
    document.getElementById("enhancedImage");

const originalSize =
    document.getElementById("originalSize");

const enhancedSize =
    document.getElementById("enhancedSize");

const enhanceButton =
    document.getElementById("enhanceButton");

const resetButton =
    document.getElementById("resetButton");

const downloadButton =
    document.getElementById("downloadButton");

const loading =
    document.getElementById("loading");


let selectedFile = null;


dropZone.addEventListener("click", () => {

    fileInput.click();

});


fileInput.addEventListener("change", () => {

    if (fileInput.files.length > 0) {

        selectFile(fileInput.files[0]);

    }

});


function selectFile(file) {

    if (!file.type.startsWith("image/")) {

        alert("Please select an image.");

        return;

    }


    selectedFile = file;


    const imageURL =
        URL.createObjectURL(file);


    originalImage.src = imageURL;


    originalImage.onload = () => {

        originalSize.textContent =
            `${originalImage.naturalWidth} × ${originalImage.naturalHeight}`;

    };


    previewSection.classList.remove("hidden");

    actionSection.classList.remove("hidden");

    downloadSection.classList.add("hidden");

    enhancedImage.src = "";

}


enhanceButton.addEventListener(
    "click",
    async () => {

        if (!selectedFile) {

            return;

        }


        enhanceButton.disabled = true;

        enhanceButton.textContent =
            "Enhancing...";


        loading.classList.remove("hidden");


        const formData = new FormData();

        formData.append(
            "file",
            selectedFile
        );


        try {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/enhance",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            const data =
                await response.json();


            if (data.error) {

                throw new Error(
                    data.error
                );

            }


            const imageURL =
                "http://127.0.0.1:8000" +
                data.download_url;


            enhancedImage.src =
                imageURL;


            enhancedImage.onload =
                () => {

                    enhancedSize.textContent =
                        `${enhancedImage.naturalWidth} × ${enhancedImage.naturalHeight}`;

                };


            downloadButton.href =
                imageURL;


            downloadSection
                .classList
                .remove("hidden");


        } catch (error) {

            alert(
                "Enhancement failed: " +
                error.message
            );

        } finally {

            loading.classList.add("hidden");

            enhanceButton.disabled = false;

            enhanceButton.textContent =
                "Enhance with AI";

        }

    }
);


resetButton.addEventListener(
    "click",
    () => {

        selectedFile = null;

        fileInput.value = "";

        originalImage.src = "";

        enhancedImage.src = "";

        previewSection.classList.add(
            "hidden"
        );

        actionSection.classList.add(
            "hidden"
        );

        downloadSection.classList.add(
            "hidden"
        );

    }
);