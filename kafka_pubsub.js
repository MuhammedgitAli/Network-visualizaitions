const { Kafka } = require('kafkajs');

const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['localhost:9092']
});

const producer = kafka.producer();
const consumer = kafka.consumer({ groupId: 'test-group' });

const topic = 'test-topic';

async function run() {
    try {
        // Connect producer and consumer
        await producer.connect();
        await consumer.connect();

        // Subscribe to topic
        await consumer.subscribe({ topic, fromBeginning: true });

        // Start consuming messages
        await consumer.run({
            eachMessage: async ({ topic, partition, message }) => {
                console.log({
                    value: message.value.toString(),
                    topic,
                    partition
                });
            },
        });

        // Produce a message
        await producer.send({
            topic,
            messages: [
                { value: 'Hello World!' },
            ],
        });

        console.log('Message sent successfully');

        // Keep the script running
        await new Promise(resolve => setTimeout(resolve, 5000));

    } catch (error) {
        console.error('Error:', error);
    } finally {
        // Disconnect producer and consumer
        await producer.disconnect();
        await consumer.disconnect();
    }
}

run().catch(console.error); 