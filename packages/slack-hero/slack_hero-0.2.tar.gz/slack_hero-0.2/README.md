# slack_hero

An internal package to use to send exceptions to slack

## Usage

1. Install the package in your application.

        pip install slack_hero

2. Add the folowing environment variables to your environment

        SLACK_BOT_TOKEN - auth token for your slack application. You might have to create a slack application and add it to the target channel.(https://api.slack.com/apps)

        CHANNEL - slack channel to which the messages should be sent

3. Import the log module

        import slack_hero.log

3. Configure your logger to send exceptions to slack as below

        LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
        },
        'handlers': {
            'slack_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'slack_hero.log.SlackExceptionHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': [ 'slack_admins'],
                'propagate': True,
            },
        },
        }
