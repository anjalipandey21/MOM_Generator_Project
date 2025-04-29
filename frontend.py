<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MOM Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f6f8;
        }
        textarea {
            width: 100%;
            height: 200px;
            margin-bottom: 20px;
            padding: 10px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            margin-bottom: 20px;
        }
        #output {
            white-space: pre-wrap;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            font-size: 16px;
        }
    </style>
</head>
<body>

    <h1>MOM Generator (Automated)</h1>

    <textarea id="ragInput" placeholder="Paste RAG output here..."></textarea>
    <br>
    <button onclick="generateMOM()">Generate MOM</button>

    <h2>Generated Minutes of Meeting (MOM):</h2>
    <div id="output"></div>

    <script>
        async function generateMOM() {
            const inputText = document.getElementById('ragInput').value;
            const outputDiv = document.getElementById('output');

            if (!inputText.trim()) {
                outputDiv.innerText = "Please paste RAG output before submitting.";
                return;
            }

            outputDiv.innerText = "Generating MOM, please wait...";

            try {
                const response = await fetch('http://localhost:8000/generate-mom
