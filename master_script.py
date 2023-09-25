import boto3
import sys
import re

def verify_email_identity(email):
    ses_client = boto3.client("ses", region_name="us-east-1")

    response = ses_client.get_identity_verification_attributes(
        Identities=[email]
    )

    status = response['VerificationAttributes'][email]['VerificationStatus']

    if status == 'Pending':
        return 'Verification email was already sent - check your inbox and/or spam folder!'
    
    elif status == 'Success':
        return 'Your email was already verified!'

    else:
        response = ses_client.verify_email_identity(
            EmailAddress=email
        )
        return 'Verification email was sent - check your inbox and/or spam folder!'

def send_plain_email(email, url):
    ses_client = boto3.client("ses", region_name="us-east-1")
    CHARSET = "UTF-8"

    response = ses_client.send_email(
        Destination={
            "ToAddresses": [
                email,
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": "Here is your file: " + url,
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "Testing File Send",
            },
        },
        Source="artiamastest@gmail.com",
    )


def createS3File(username):
    s3_client = boto3.client('s3')

    # deposit instructions for instance
    data_s3_bucket = 'artiamas-testing-bucket'
    target_file = username + "/test.txt"
    out = "Hello %s!" % (username)

    s3_client.put_object(Body=out,
                         Bucket=data_s3_bucket,
                         Key=target_file)
    
    url = "https://artiamas-testing-bucket.s3.amazonaws.com/" + username + "/test.txt"
    return url


def master(username, email):
    url = createS3File(username)
    send_plain_email(email, url)
    return("You were emailed a file!")
    
# for testing email verification with specific domains
def cmd_verification_test(email):

    pattern = r"\w*(.edu|.army.mil)$"
    match = re.search(pattern, email) 
    
    if match != None: 
        return verify_email_identity(email)

    else:
        return "please enter a valid email with an .edu or .army.mil domain!"


if __name__ =="__main__":  
    cmd = sys.argv[1]
    email = sys.argv[2]

    if cmd == "email_auth_verify":
        ret = cmd_verification_test(email)
        print(ret)


    if cmd == "verify_email_ses":
        ret = verify_email_identity(email)
        print(ret)

    if cmd == "new_run":
        master(email)
