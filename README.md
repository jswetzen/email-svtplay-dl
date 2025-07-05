# email-svtplay-dl

## Overview

`email-svtplay-dl` is a minimal system for automatically downloading videos from SVT Play or TV4 Play links received via email. It is designed to run in a containerized environment and leverages `fetchmail`, a custom email parser, and `svtplay-dl` to automate the process.

## Features

- Polls a mail server for new messages at a configurable interval
- Extracts SVT Play or TV4 Play URLs from incoming emails
- Downloads videos using `svtplay-dl` with customizable options
- Runs easily in Docker

## Components

- **Dockerfile**: Sets up the environment with all dependencies
- **run.sh**: Entrypoint script that configures fetchmail and starts polling
- **mailtrigger.sh**: Triggered by fetchmail to process new emails and start downloads
- **parsemailurl.py**: Extracts video URLs from email content
- **tests/**: Contains unit tests for the email parsing logic

## Quick Start

### 1. (Optional) Build the Docker Image

If you don't want to use the pre-built at `ghcr.io/jswetzen/email-svtplay-dl:main`, build it with

```sh
docker build -t ghcr.io/jswetzen/email-svtplay-dl:main .
```

### 2. Configure Environment Variables

You can override these defaults when running the container:

- `POLL_INTERVAL`: How often (in seconds) to poll for new mail (default: 300)
- `FETCHMAIL_DEF`: Fetchmail configuration string (see below)
- `DL_OPTIONS`: Options passed to `svtplay-dl` (default: `-S --all-subtitles`)

Example `FETCHMAIL_DEF`:

```
poll mail.example.com proto pop3 port 110 user mail@example.com password pass
```

### 3. Run the Container

```sh
docker run -e POLL_INTERVAL=300 \
           -e FETCHMAIL_DEF="poll mail.example.com proto pop3 port 110 user mail@example.com password pass" \
           -e DL_OPTIONS="-S --all-subtitles" \
           -v /your/download/dir:/data \
           ghcr.io/jswetzen/email-svtplay-dl:main
```

All downloaded files will appear in `/your/download/dir` on the host.

## How It Works

1. **run.sh** sets up fetchmail with your configuration and starts polling for new mail.
2. When a new email arrives, fetchmail calls **mailtrigger.sh**.
3. **mailtrigger.sh** runs **parsemailurl.py** to extract the first SVT Play or TV4 Play URL from the email body.
4. The extracted URL is passed to `svtplay-dl` (with your options) to download the video.

## Customization

- Change `DL_OPTIONS` to adjust how `svtplay-dl` downloads videos (see [svtplay-dl documentation](https://svtplay-dl.se/)).
- Adjust `FETCHMAIL_DEF` for your mail provider and credentials.

## Testing

Unit tests for the email parser are in `tests/test_parsemailurl.py`. To run them:

```sh
python3 -m unittest discover tests
```

## Security Notes

- The container expects to run as root (for fetchmail config). Do not expose sensitive credentials in public environments.
- Use app passwords or limited-scope credentials for mail access.

## Troubleshooting

- Check container logs for errors with fetchmail or svtplay-dl.
- Ensure your mail provider allows POP3/IMAP access.
- Make sure the download directory is writable by the container.

## License

MIT License. See `LICENSE` file.
