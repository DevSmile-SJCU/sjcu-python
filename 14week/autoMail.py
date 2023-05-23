import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 발신자 정보
sender_email = "your_email@naver.com"
sender_password = "your_password"

# 수신자 정보
recipient_email = "recipient_email@example.com"

# 이메일 제목과 내용
subject = "네이버 메일을 통한 이메일 발송"
body = "안녕하세요, 이메일 내용입니다."

# MIME 멀티파트 메시지 생성
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject

# 메일 내용 추가
message.attach(MIMEText(body, "plain"))

# SMTP 서버 연결
smtp_server = "smtp.naver.com"
smtp_port = 465

try:
    smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    smtp.login(sender_email, sender_password)

    # 이메일 발송
    smtp.sendmail(sender_email, recipient_email, message.as_string())
    smtp.quit()

    print("이메일 발송 성공")
except Exception as e:
    print("이메일 발송 실패:", str(e))
