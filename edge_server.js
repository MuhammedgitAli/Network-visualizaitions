const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/process', async (req, res) => {
    // Simulate edge processing delay (10ms)
    await new Promise(resolve => setTimeout(resolve, 10));
    
    res.json({
        status: 'success',
        processing_time: '10ms',
        location: 'edge',
        timestamp: new Date().toISOString()
    });
});

app.listen(port, () => {
    console.log(`Edge server running at http://localhost:${port}`);
}); 