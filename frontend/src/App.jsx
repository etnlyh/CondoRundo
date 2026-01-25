import { useState } from 'react';
import './App.css';

function App() {
  const [size, setSize] = useState('');
  const [rooms, setRooms] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    if (!size || !rooms) {
      alert("Please enter both size and rooms");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch(`http://127.0.0.1:8000/price?size=${size}&rooms=${rooms}`);
      if (!response.ok) throw new Error("Server error");

      const data = await response.json();
      setPrediction(data);
    } catch (error) {
      console.error("Connection failed:", error);
      alert("Make sure your FastAPI server is running on port 8000!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>House Predictor</h1>

      <div className="input-group">
        <input
          type="number"
          placeholder="Size (sq ft)"
          value={size}
          step={50}
          onChange={(e) => setSize(e.target.value)}
        />
      </div>

      <div className="input-group">
        <input
          type="number"
          placeholder="Number of Rooms"
          value={rooms}
          onChange={(e) => setRooms(e.target.value)}
        />
      </div>

      <button onClick={handlePredict} disabled={loading}>
        {loading ? 'Processing...' : 'Calculate Price'}
      </button>

      {prediction && (
        <div className="result-card">
          <h3>Estimation</h3>
          <p>Properties: {prediction.size} sq ft, {prediction.rooms} rooms</p>
          <p className="price-text">
            CAD ${prediction.estimated_price_cad.toLocaleString()}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
