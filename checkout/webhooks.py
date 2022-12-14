import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import WebhookHandler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listens for webhooks
    from Stripe
    """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    event = None
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
        # Invalid payload
    except ValueError as e:
        return HttpResponse(status=400)
        # Invalid signature
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
        # All other exceptions
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up a webhook handler
    handler = WebhookHandler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
