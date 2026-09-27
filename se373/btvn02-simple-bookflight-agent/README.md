# Simple Flight Booking Agent

## Overview

This is a command-line flight assistant built with LangChain and LangGraph. It uses an OpenRouter-hosted language model to search the included sample flight data, list available flights, show flight details, and summarize a selected flight.

The project uses in-memory data and conversation state, so it does not make real bookings or save information after the program stops.

## Features

- Search flights by route and departure date.
- Browse the available sample flights.
- View and summarize flight details.
- Chat through a simple terminal interface.

## How to Set Up Locally

### Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/)
- An OpenRouter API key and supported model ID

### Installation

1. Open the project directory:

   ```bash
   cd se373/btvn02-simple-bookflight-agent
   ```

2. Install the dependencies:

   ```bash
   uv sync
   ```

3. Open `src/llm.py` and replace these placeholders with your OpenRouter details:

   ```python
   model="paste-your-model-id-here"
   api_key=SecretStr("paste-your-api-key-here")
   ```

   Keep your real API key private and do not commit it to Git.

4. Start the agent:

   ```bash
   uv run python main.py
   ```

## Usage

Enter a flight request in the terminal. Type `exit` to close the program.
