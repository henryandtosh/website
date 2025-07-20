# Henry & Tosh Limited - Website

A professional, responsive website for Henry & Tosh Limited, a UK-based private investment company focused on trading synthetic options on MicroStrategy Inc. (MSTR).

## 🚀 Features

- **Professional Design**: Clean, minimalist design with institutional styling
- **Mobile Responsive**: Fully responsive design that works on all devices
- **Smooth Animations**: Subtle animations and transitions for enhanced UX
- **Contact Form**: Functional contact form with validation
- **Performance Metrics**: Animated performance statistics
- **SEO Optimized**: Proper meta tags and semantic HTML structure

## 📁 File Structure

```
WEBSITE/
├── index.html          # Main homepage
├── styles.css          # All styling and responsive design
├── script.js           # Interactive functionality
├── README.md           # This file
├── specification.md    # Original website specification
└── favicon.ico         # Website favicon
```

## 🛠️ Setup Instructions

### Local Development

1. **Clone or Download** the website files to your local machine
2. **Open** `index.html` in your web browser
3. **Test** all functionality including:
   - Navigation menu (desktop and mobile)
   - Contact form submission
   - Smooth scrolling between sections
   - Responsive design on different screen sizes

### Deployment

#### Option 1: Static Hosting (Recommended)
- Upload all files to any static hosting service:
  - Netlify
  - Vercel
  - GitHub Pages
  - AWS S3
  - Any web hosting provider

#### Option 2: WordPress Integration
- Convert to WordPress theme by:
  - Creating a WordPress theme structure
  - Moving content to WordPress pages/posts
  - Using WordPress form plugins for contact functionality

#### Option 3: Traditional Web Hosting
- Upload files via FTP to your web hosting provider
- Ensure SSL certificate is installed
- Configure domain DNS settings

## 🎨 Design Specifications

### Color Palette
- **Primary**: Dark Navy (#1e3a8a)
- **Secondary**: Black (#1a1a1a)
- **Background**: White (#fff)
- **Accent**: Grey (#f8fafc, #e2e8f0)

### Typography
- **Headings**: Roboto Slab (serif)
- **Body Text**: Inter (sans-serif)
- **Font Weights**: 300, 400, 500, 600, 700

### Layout
- **Container Width**: 1200px max-width
- **Grid System**: CSS Grid and Flexbox
- **Spacing**: Consistent 8px base unit system

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: Below 768px
- **Small Mobile**: Below 480px

## 🔧 Customization

### Content Updates
- Edit `index.html` to update company information
- Modify performance statistics in the Performance section
- Update contact details and company registration information

### Styling Changes
- Edit `styles.css` to modify colors, fonts, or layout
- Update CSS custom properties for easy theme changes
- Modify responsive breakpoints as needed

### Functionality
- Edit `script.js` to add new interactive features
- Modify form handling for backend integration
- Add analytics or tracking code

## 📧 Contact Form Integration

The contact form currently simulates submission. To integrate with a backend:

1. **Email Service** (Recommended):
   - Netlify Forms
   - Formspree
   - EmailJS
   - Custom PHP/Node.js backend

2. **Update the form submission in `script.js`**:
   ```javascript
   // Replace the setTimeout with actual API call
   fetch('/api/contact', {
       method: 'POST',
       headers: { 'Content-Type': 'application/json' },
       body: JSON.stringify(data)
   })
   ```

## 🔒 Security Considerations

- **SSL Certificate**: Ensure HTTPS is enabled
- **Form Validation**: Client-side validation implemented
- **XSS Protection**: Input sanitization recommended for backend
- **Privacy**: No third-party trackers included

## 📊 Performance Optimization

- **Minified Assets**: Consider minifying CSS/JS for production
- **Image Optimization**: Add optimized images as needed
- **Caching**: Implement browser caching headers
- **CDN**: Use CDN for faster global delivery

## 🚀 Future Enhancements

Based on the specification, potential future features:

1. **Secure Investor Portal**: For counterparty access
2. **Live Performance Tracker**: Real-time performance updates
3. **Companies House Integration**: Real-time company status
4. **Blog/News Section**: Company updates and market insights
5. **Multi-language Support**: International expansion

## 📞 Support

For technical support or customization requests:
- Email: admin@henryandtosh.com
- Company: Henry & Tosh Limited
- Registered Office: Sherwood, Lower Seagry, Chippenham, SN15 5EP

## 📄 Legal

- **Copyright**: © 2024 Henry & Tosh Limited
- **Company Registration**: 11919030 (England & Wales)
- **Disclaimer**: This website is for informational purposes only and does not constitute an offer to invest.

---

*Built with modern web technologies for optimal performance and user experience.* 