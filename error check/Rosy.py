<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python Editor with Error Highlighting</title>

  <!-- CodeMirror CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.9/codemirror.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.9/theme/material.css">

  <!-- CodeMirror JS and Python Mode -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.9/codemirror.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.9/mode/python/python.min.js"></script>

  <!-- Pyodide for Python Execution in Browser -->
  <script src="https://cdn.jsdelivr.net/pyodide/v0.22.0/full/pyodide.js"></script>

  <style>
    /* Style the error message */
    #error-message {
      color: red;
      font-size: 0.9em;
      margin-top: 10px;
    }
  </style>
</head>
<body>

<h2>Python Editor with Error Highlighting</h2>
<textarea id="codeEditor"># Write your Python code here!</textarea>
<div id="error-message"></div>

<script>
  // Load Pyodide
  let pyodideReady = false;
  async function loadPyodideAndPackages() {
    self.pyodide = await loadPyodide();
    pyodideReady = true;
  }
  loadPyodideAndPackages();

  // Initialize CodeMirror
  const editor = CodeMirror.fromTextArea(document.getElementById("codeEditor"), {
    mode: "python",               // Python mode
    theme: "material",            // Theme for the editor
    lineNumbers: true,            // Show line numbers
  });

  // Function to check for errors in Python code
  async function checkPythonCode() {
    const code = editor.getValue();
    const errorMessageDiv = document.getElementById("error-message");
    errorMessageDiv.textContent = ""; // Clear previous error message

    if (pyodideReady) {
      try {
        // Run the code in Pyodide and catch any errors
        await pyodide.runPythonAsync(code);
      } catch (error) {
        // Display the error message
        errorMessageDiv.textContent = `Error: ${error.message}`;
        console.error(error); // Optional: log the error in the console
      }
    }
  }

  // Run error check when the editor content changes
  editor.on("change", () => {
    checkPythonCode();
  });
</script>

</body>
</html>
