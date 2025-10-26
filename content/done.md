Title: Done List
Date: 2017-06-15 15:15
Category: todo

- AWS (EC2, S3, Route 53, RDS, Lambda, ECR, SNS, SQS, SES, IAM, Inspector)
- docker, docker-compose
- python
- ansible
- jenkins
- Let's Encrypt:
    - Slack command -> Python RTM bot -> Jenkins Job for new subdomain
    - Jenkins Periodical Job for SSL renew -> Slack report
    - SSL certs info page for all subdomains (Python, bottle, uWISGI in Docker, Nginx)
- GitHub, GitLab, Gogs, gitolite (+ Jenkins and Slack integrations)
- Golang (simple dockerized services: Slack slash command, Slach help bot)
- CI/CD:
    - Git push -> Jenkins tests & builds, OWASP Dependency-Check analysis -> Docker Registry -> [Jenkins deploy]
    - Slack command -> Python RTM bot -> Jenkins deploy -> Slack notification
- Monitoring:
    - Zabbix -> Slack
    - AWS CloudWatch -> AWS SNS -> AWS Lambda -> Slack
