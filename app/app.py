import streamlit as st
from sklearn.pipeline import Pipeline
from text_processing import TextPreprocessor
from joblib import load

# Load the trained model pipeline
model = load("customer_support_pipeline.pkl")

# Dictionary mapping intents to corresponding responses
intent_responses = {
    "edit_account": "To edit your account information, please go to the 'Account Settings' page.",
    "switch_account": "You can switch between multiple accounts using the account switcher in the top-right corner.",
    "check_invoice": "To check your invoices, please visit the 'Billing' section of your account.",
    "complaint": "We appreciate your feedback. Please provide more details about your complaint so we can assist you better.",
    "contact_customer_service": "You can reach our customer service team at [phone number] or [email address].",
    "delivery_period": "Delivery times vary depending on your location and the shipping method chosen during checkout.",
    "registration_problems": "If you're experiencing trouble registering, please ensure you're using a valid email address and meet the password requirements.",
    "check_payment_methods": "We accept the following payment methods: [List payment methods].",
    "contact_human_agent": "I can connect you with a human agent. Please hold while I transfer you.",
    "payment_issue": "We apologize for the payment issue. Please verify your payment information or contact your bank.",
    "newsletter_subscription": "To subscribe to our newsletter, enter your email address in the 'Subscribe' box at the bottom of the page.",
    "get_invoice": "You can download your invoices from the 'Order History' section.",
    "place_order": "To place an order, simply add the desired items to your cart and proceed to checkout.",
    "cancel_order": "You can cancel your order before it ships. Please contact customer support for assistance.",
    "track_refund": "Once your refund is processed, you'll receive a confirmation email with tracking information.",
    "change_order": "Order modifications may be possible depending on the order status. Please contact us.",
    "get_refund": "Refunds are eligible for returns within [number] days of purchase.",
    "create_account": "Creating an account is easy! Just click on 'Sign Up' and follow the instructions.",
    "check_refund_policy": "Our refund policy can be found on our website, under 'Terms and Conditions'.",
    "review": "We appreciate your feedback! Please leave your review on our product page.",
    "set_up_shipping_address": "You can add or edit shipping addresses in the 'Address Book' section of your account.",
    "delivery_options": "We offer various shipping options, including standard and express delivery.",
    "delete_account": "We're sorry to hear you'd like to delete your account. You can do so in the 'Account Settings'.",
    "recover_password": "To reset your password, click on 'Forgot Password' and follow the instructions sent to your email.",
    "track_order": "You can track your order status using the tracking number provided in your confirmation email.",
    "change_shipping_address": "Address changes are possible before shipment. Please contact us immediately.",
    "check_cancellation_fee": "Cancellation fees may apply depending on the order. Please review our cancellation policy."
}

def chatbot(text):
    intent = model.predict([text])[0]
    if intent in intent_responses:
        return intent_responses[intent]
    else:
        return "Sorry, I didn't understand your request. Please try rephrasing."

# Streamlit interface
st.title("Customer Support Chatbot")

user_input = st.text_input("Enter your message:")

if user_input:
    response = chatbot(user_input)
    st.write(f"Chatbot: {response}")