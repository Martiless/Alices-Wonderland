/* Logic for Stripe payments */

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
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
        color: 'irebrick',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');