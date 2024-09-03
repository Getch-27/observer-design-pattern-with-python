# Weather Condition Notifier

This small project demonstrates the Observer design pattern using Python and Docker. The application allows users to subscribe to specific weather conditions and get notified when those conditions are reported.

## Features

1. **Observers/Subscribers Subscription**: Users can subscribe to weather conditions of their interest (e.g., cold, warm).

2. **Weather Condition Check**: The subject checks the current weather condition

3. **Notification**: Observers are notified if the current weather condition matches their subscription.


## Setup

### Docker

1. **Build the Docker Image**:

   ```bash
   docker build -t observer-example .
   docker run observer-example
