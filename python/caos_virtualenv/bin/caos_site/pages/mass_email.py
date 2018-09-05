from django.core.mail import get_connection, EmailMultiAlternatives

def send_mass_html_mail(subject, email_template, email_context, to_list):
    """
    Given a datatuple of (subject, text_content, html_content, from_email,
    recipient_list), sends each message to each recipient list. Returns the
    number of emails sent.

    If from_email is None, the DEFAULT_FROM_EMAIL setting is used.
    If auth_user and auth_password are set, they're used to log in.
    If auth_user is None, the EMAIL_HOST_USER setting is used.
    If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.

    """
    connection = get_connection()
    html_content = render_to_string(email_template, email_context)
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, "no-reply@caos.cs.siue.edu", to_list, connection=connection)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    connection.close()