# Delete Orphan Device for Home Assistant

A lightweight Home Assistant custom component that adds an action/service to forcefully remove orphaned devices from the device registry by their `device_id`.

## Installation

### Via Custom Repository in HACS:
1. Push this repository to GitHub.
2. In Home Assistant, open **HACS** > **Integrations**.
3. Click the **3 dots** in the top-right corner > **Custom repositories**.
4. Paste your GitHub repository URL and select Category **Integration**.
5. Click **Add**, then find and install **Delete Orphan Device**.
6. Restart Home Assistant.
7. Go to **Settings** > **Devices & Services** > **Add Integration** and search for **Delete Orphan Device**.

## Usage

1. Go to **Developer Tools** > **Actions** (or **Services**).
2. Select **Delete Orphan Device: remove_device** (`delete_orphan.remove_device`).
3. Enter your device ID:
   ```yaml
   device_id: 4177ce77b90c6bf8dba5ebb516be2610
   ```
4. Click **Perform Action** / **Call Service**.
