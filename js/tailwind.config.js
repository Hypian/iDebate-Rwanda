var siteTailwindConfig = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'surface-container-low': '#fcf2ec',
        'border-hairline': '#DDD3C1',
        'on-tertiary': '#ffffff',
        'on-tertiary-fixed': '#111c2d',
        'on-surface': '#1f1b18',
        'terracotta-sun': '#D97745',
        'forest-deep': '#0E2419',
        'tertiary-fixed-dim': '#bcc7de',
        'on-primary-container': '#fffbff',
        'on-error': '#ffffff',
        'secondary-fixed-dim': '#abcfb8',
        'surface-bright': '#fff8f5',
        'ochre-sand': '#E8B058',
        'on-tertiary-fixed-variant': '#3c475a',
        'on-background': '#1f1b18',
        'inverse-primary': '#ffb596',
        'on-secondary-container': '#496a57',
        'on-primary-fixed': '#360f00',
        'inverse-on-surface': '#f9efea',
        'outline-variant': '#ddc1b6',
        'primary-fixed': '#ffdbcd',
        'on-primary-fixed-variant': '#7d2d00',
        'on-tertiary-container': '#fefcff',
        'surface-container-lowest': '#ffffff',
        'on-primary': '#ffffff',
        'secondary-container': '#c4e8d1',
        'paper-surface': '#F2ECE1',
        'tertiary-fixed': '#d8e3fb',
        'secondary': '#456553',
        'secondary-fixed': '#c7ebd4',
        'paper-canvas': '#FAF7F2',
        'surface-container': '#f6ece7',
        'tertiary-container': '#6a758a',
        'surface-variant': '#ebe0db',
        'on-secondary': '#ffffff',
        'surface-container-highest': '#ebe0db',
        'surface-container-high': '#f0e6e1',
        'on-surface-variant': '#56423b',
        'on-secondary-fixed': '#002113',
        'error-container': '#ffdad6',
        'on-secondary-fixed-variant': '#2d4d3c',
        'inverse-surface': '#352f2c',
        'primary': '#9a4111',
        'surface-tint': '#9d4314',
        'on-error-container': '#93000a',
        'surface-dim': '#e2d8d3',
        'outline': '#897269',
        'background': '#fff8f5',
        'primary-container': '#ba5828',
        'tertiary': '#515c71',
        'primary-fixed-dim': '#ffb596',
        'surface': '#fff8f5',
        'error': '#ba1a1a'
      },
      borderRadius: {
        DEFAULT: '0.25rem',
        lg: '0.5rem',
        xl: '0.75rem',
        full: '9999px'
      },
      spacing: {
        'margin-tablet': '2.5rem',
        'gutter-desktop': '2.5rem',
        'space-xs': '0.375rem',
        'margin-desktop': '4.5rem',
        'space-xl': '3.5rem',
        margin: '1.25rem',
        gutter: '1.5rem',
        'space-lg': '2rem',
        'space-md': '1.25rem',
        'space-sm': '0.75rem'
      },
      fontFamily: {
        'quote-display': ['Newsreader', 'serif'],
        'headline-xl-mobile': ['Newsreader', 'serif'],
        'headline-sm': ['Newsreader', 'serif'],
        'body-xl': ['Manrope', 'sans-serif'],
        'headline-lg': ['Newsreader', 'serif'],
        'body-lg': ['Manrope', 'sans-serif'],
        'display-hero': ['Newsreader', 'serif'],
        'label-md': ['Manrope', 'sans-serif'],
        'body-md': ['Manrope', 'sans-serif'],
        'headline-md': ['Newsreader', 'serif'],
        'label-caps': ['Manrope', 'sans-serif'],
        'display-hero-mobile': ['Newsreader', 'serif'],
        'headline-xl': ['Newsreader', 'serif']
      },
      fontSize: {
        'quote-display': ['28px', { lineHeight: '40px', letterSpacing: '-0.01em', fontWeight: '400' }],
        'headline-xl-mobile': ['30px', { lineHeight: '38px', letterSpacing: '-0.01em', fontWeight: '400' }],
        'headline-sm': ['20px', { lineHeight: '28px', fontWeight: '600' }],
        'body-xl': ['19px', { lineHeight: '32px', fontWeight: '400' }],
        'headline-lg': ['32px', { lineHeight: '40px', letterSpacing: '-0.01em', fontWeight: '500' }],
        'body-lg': ['16px', { lineHeight: '26px', fontWeight: '400' }],
        'display-hero': ['56px', { lineHeight: '64px', letterSpacing: '-0.02em', fontWeight: '400' }],
        'label-md': ['13px', { lineHeight: '18px', fontWeight: '600' }],
        'body-md': ['14px', { lineHeight: '22px', fontWeight: '400' }],
        'headline-md': ['24px', { lineHeight: '32px', fontWeight: '500' }],
        'label-caps': ['12px', { lineHeight: '16px', letterSpacing: '0.08em', fontWeight: '700' }],
        'display-hero-mobile': ['38px', { lineHeight: '44px', letterSpacing: '-0.01em', fontWeight: '400' }],
        'headline-xl': ['40px', { lineHeight: '48px', letterSpacing: '-0.015em', fontWeight: '400' }]
      }
    }
  }
};

if (typeof tailwind !== 'undefined') {
  tailwind.config = siteTailwindConfig;
}

if (typeof module !== 'undefined') {
  module.exports = siteTailwindConfig;
}
