from django.http import HttpResponse


class WebhookHandler:
    """
    Handles Stripes Webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles all webhook events
        """
        return HttpResponse(
            content=f'Unhandled webhook received for {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handles successful payment_intent webhooks
        from Stripe
        """
        intent = event.data.object
        print(intent)

        return HttpResponse(
            content=f'Payment successful webhook received for {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles failed payment_intent webhooks
        from Stripe
        """
        return HttpResponse(
            content=f'Payment failed webhook received for {event["type"]}',
            status=200)
