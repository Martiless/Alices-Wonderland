/* Logic for Stripe payments */

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe('pk_test_51LdYGOGScmbyNe5yNX8o0lHL9e3h9ijtPvKgMMZkoamDFGadEWOL6E03UFQewAsnEEO8VBdWRuhmPPuHCaaw0kdQ00LxW4XcTV');
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: 'Lora',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: 'firebrick',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

/* Handles realtime validation on card elements */
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
        <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = ''
    }
});

/* Handle form submission */

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disable': true});
    $('#submit-button').attr('disable', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
        var html = `
        <span>${result.error.message}</span>
        `;
        $(errorDiv).html(html);
        card.update({'disable': false});
        $('#submit-button').attr('disable', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.onsubmit();
            }
        }
        
    })
})
