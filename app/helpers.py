import boto3

def send_email(to_email, subject, body):
    client = boto3.client(
        'ses',
        aws_access_key_id=ks[0],
        aws_secret_access_key=ks[1],
        region_name='ap-northeast-1')
    response = client.send_email(
        Destination={
            #'BccAddresses': [
            #],
            #'CcAddresses': [
            #    'recipient3@example.com',
            #],
            'ToAddresses': [
                to_email,
            ],
        },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': body,
            },
        },
        'Subject': {
        'Charset': 'UTF-8',
            'Data': subject,
        },
    },
        #ReplyToAddresses=[
        #],
        #ReturnPath='',
        #ReturnPathArn='',
        Source='moogoo78@gmail.com',
        #SourceArn='',
    )

    return response
