const express = require('express');
const app = express();
const port = 4000;

app.use(express.json());

app.get('/process', async (req, res) => {
    // Simulate cloud processing delay (100ms)
    await new Promise(resolve => setTimeout(resolve, 100));
    
    res.json({
        status: 'success',
        processing_time: '100ms',
        location: 'cloud',
        timestamp: new Date().toISOString()
    });
});

app.listen(port, () => {
    console.log(`Cloud server running at http://localhost:${port}`);
}); 