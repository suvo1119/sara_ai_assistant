import type { AppConfig } from './lib/types';

export const APP_CONFIG_DEFAULTS: AppConfig = {
  companyName: 'Sara',
  pageTitle: 'Sara',
  pageDescription: 'Sara - Your cute AI assistant 💕',

  supportsChatInput: true,
  supportsVideoInput: true,
  supportsScreenShare: true,
  isPreConnectBufferEnabled: true,

  logo: '/sara.png',
  accent: '#ff69b4',
  logoDark: '/sara.png',
  accentDark: '#ff91c8',
  startButtonText: 'Talk To Sara 💕',

  agentName: undefined,
};
