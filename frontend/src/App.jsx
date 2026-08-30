import { useState } from "react";
import "./App.css";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);

  function handleFileChange(event) {
    const file = event.target.files[0];

    if (file) {
      setSelectedFile(file);
    }
  }

  return (
    <main className="docuai-app">

      {/* Hero Section */}
      <section className="hero">

        <div className="ai-icon">
          <div className="icon-orbit orbit-one"></div>
          <div className="icon-orbit orbit-two"></div>

          <span>✦</span>
        </div>

        <div className="hero-content">
          <div className="badge">
            <span className="pulse-dot"></span>
            AI DOCUMENT INTELLIGENCE
          </div>

          <h1>
            Docu<span>AI</span>
          </h1>

          <p className="subtitle">
            Enterprise Multimodal AI Document Intelligence Platform
          </p>

          <p className="description">
            Upload documents, extract information, classify content,
            and transform unstructured data into intelligent insights.
          </p>
        </div>

      </section>


      {/* Upload Section */}
      <section className="upload-section">

        <div className="section-title">
          <div className="section-icon">⬆</div>

          <div>
            <h2>Upload Document</h2>
            <p>Start your AI-powered document analysis</p>
          </div>
        </div>


        <label className="upload-card">

          <input
            type="file"
            accept=".pdf,.jpg,.jpeg,.png"
            onChange={handleFileChange}
          />

          <div className="upload-animation">
            <div className="upload-ring ring-one"></div>
            <div className="upload-ring ring-two"></div>

            <div className="file-icon">📄</div>
          </div>

          {selectedFile ? (
            <>
              <h3 className="file-selected">
                {selectedFile.name}
              </h3>

              <p>
                File selected successfully ✓
              </p>
            </>
          ) : (
            <>
              <h3>Drop your document here</h3>

              <p>
                PDF, JPG, JPEG or PNG
              </p>

              <span className="choose-file">
                Choose File
              </span>
            </>
          )}

        </label>

      </section>


      {/* Feature Cards */}
      <section className="features">

        <div className="feature-card">
          <div className="feature-icon purple">◈</div>

          <h3>Multimodal Processing</h3>

          <p>
            Process PDFs, scanned documents and images.
          </p>
        </div>


        <div className="feature-card">
          <div className="feature-icon cyan">✦</div>

          <h3>AI Classification</h3>

          <p>
            Automatically identify document types intelligently.
          </p>
        </div>


        <div className="feature-card">
          <div className="feature-icon purple">⌘</div>

          <h3>Information Extraction</h3>

          <p>
            Extract meaningful structured information.
          </p>
        </div>

      </section>


      {/* Workflow */}
      <section className="workflow">

        <div className="workflow-header">
          <div className="section-icon">⌁</div>

          <div>
            <h2>How DocuAI Works</h2>
            <p>Your intelligent document processing pipeline</p>
          </div>
        </div>


        <div className="workflow-steps">

          <div className="step">
            <div className="step-number">01</div>
            <span>Upload</span>
          </div>

          <div className="step-line"></div>

          <div className="step">
            <div className="step-number">02</div>
            <span>Extract</span>
          </div>

          <div className="step-line"></div>

          <div className="step">
            <div className="step-number">03</div>
            <span>Classify</span>
          </div>

          <div className="step-line"></div>

          <div className="step">
            <div className="step-number">04</div>
            <span>Analyze</span>
          </div>

        </div>

      </section>

    </main>
  );
}

export default App;