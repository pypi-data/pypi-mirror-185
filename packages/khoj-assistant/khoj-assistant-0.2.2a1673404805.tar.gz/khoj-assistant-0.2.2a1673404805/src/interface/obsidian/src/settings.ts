import { App, PluginSettingTab, request, Setting } from 'obsidian';
import Khoj from 'src/main';
import { getVaultAbsolutePath } from 'src/utils';

export interface KhojSetting {
    resultsCount: number;
    khojUrl: string;
    obsidianVaultPath: string;
    connectedToBackend: boolean;
}

export const DEFAULT_SETTINGS: KhojSetting = {
    resultsCount: 6,
    khojUrl: 'http://localhost:8000',
    obsidianVaultPath: getVaultAbsolutePath(),
    connectedToBackend: false,
}

export class KhojSettingTab extends PluginSettingTab {
    plugin: Khoj;

    constructor(app: App, plugin: Khoj) {
        super(app, plugin);
        this.plugin = plugin;
    }

    display(): void {
        const { containerEl } = this;
        containerEl.empty();

        // Add notice if unable to connect to khoj backend
        if (!this.plugin.settings.connectedToBackend) {
            containerEl.createEl('small', { text: '❗Ensure Khoj backend is running and Khoj URL is correctly set below' });
        }

        // Add khoj settings configurable from the plugin settings tab
        new Setting(containerEl)
            .setName('Vault Path')
            .setDesc('The Obsidian Vault to search with Khoj')
            .addText(text => text
                .setValue(`${this.plugin.settings.obsidianVaultPath}`)
                .onChange(async (value) => {
                    this.plugin.settings.obsidianVaultPath = value;
                    await this.plugin.saveSettings();
                }));
        new Setting(containerEl)
            .setName('Khoj URL')
            .setDesc('The URL of the Khoj backend')
            .addText(text => text
                .setValue(`${this.plugin.settings.khojUrl}`)
                .onChange(async (value) => {
                    this.plugin.settings.khojUrl = value;
                    await this.plugin.saveSettings();
                }));
         new Setting(containerEl)
            .setName('Results Count')
            .setDesc('The number of search results to show')
            .addText(text => text
                .setPlaceholder('6')
                .setValue(`${this.plugin.settings.resultsCount}`)
                .onChange(async (value) => {
                    this.plugin.settings.resultsCount = parseInt(value);
                    await this.plugin.saveSettings();
                }));
        new Setting(containerEl)
            .setName('Index Vault')
            .setDesc('Manually force Khoj to re-index your Obsidian Vault')
            .addButton(button => button
                .setButtonText('Update')
                .setCta()
                .onClick(async () => {
                    await request(`${this.plugin.settings.khojUrl}/api/update?t=markdown&force=true`);
                }
            ));
    }
}
