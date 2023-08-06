* Requirements
  * Two directories must exist in the root of the project
    - tokens
    - logs
  * Two config variables must be set in the app config
    - SERVICEFUSION_CLIENT_ID
    - SERVICEFUSION_CLIENT_SECRET
- Package uses Client_Credentials authentication, because authorization code flow is broken locally for the SF api. 