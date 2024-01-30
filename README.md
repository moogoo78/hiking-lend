# Hiking-lend

## System

Built by:
- Web App: Python (Flask)
- Database: PostgreSQL
- Front-end Framework: [UIkit](https://getuikit.com/)

## Design

### 流程概略

```mermaid
flowchart TD
    Start[使用者] --> User(Registration?)
    User --> Calendar(選擇租借日期)
    User --> Store(選擇租借店家)
    Calendar --> Lend(填寫租借單-聯絡資訊)
    Store --> Lend
    Lend --> StoreConfig{店家設定}
    StoreConfig -- 線下聯絡 --> ContactInfo(顯示聯絡資訊)
    StoreConfig -- 直接付款 --> Payment(進入第三方支付頁面)
    ContactInfo --> UserContact[使用者聯絡店家]
    Payment --> 3rdPartyPayment(綠界第三方支付)
    3rdPartyPayment --> SuccessPayment(付款成功)
    3rdPartyPayment --> FailPayment(付款失敗)
    SuccessPayment --> SendEmail[寄送詳細租借email]
```

## Development

1. Install Docker

build local deployment docker image

2. docker build & up

```bash
docker compose build
'''

start local deployment environment

'''bash
docker compose up
```

### Deployment

1. Build production image

```bash
sudo docker compose -f compose.yml -f compose.prod.yml build
```

2. Start production container

```bash
sudo docker compose -f compose.yml -f compose.prod.yml up
```
