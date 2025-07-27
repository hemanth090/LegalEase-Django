# LegalEase Deployment Guide for Render

This guide will help you deploy your LegalEase application to Render for free.

## 🚀 Quick Deployment Steps

### Prerequisites
1. GitHub account
2. Render account (free at render.com)
3. Your code pushed to GitHub

### Step 1: Push Code to GitHub
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### Step 2: Deploy Backend (Django API)

1. **Go to Render Dashboard**
   - Visit https://render.com and sign in
   - Click "New +" → "Web Service"

2. **Connect Repository**
   - Connect your GitHub account
   - Select your LegalEase repository
   - Choose the main branch

3. **Configure Service**
   - **Name**: `legalease-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn legalease.wsgi:application`
   - **Plan**: `Free`

4. **Set Environment Variables**
   - `DEBUG`: `False`
   - `SECRET_KEY`: (Generate a secure key)
   - `GROQ_API_KEY`: (Your Groq API key)
   - `PYTHON_VERSION`: `3.11.0`

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Note your backend URL: `https://legalease-backend.onrender.com`

### Step 3: Deploy Frontend (React App)

1. **Create New Static Site**
   - In Render dashboard, click "New +" → "Static Site"
   - Connect same repository

2. **Configure Static Site**
   - **Name**: `legalease-frontend`
   - **Build Command**: `cd frontend && npm ci && npm run build`
   - **Publish Directory**: `frontend/build`
   - **Plan**: `Free`

3. **Set Environment Variables**
   - `REACT_APP_API_URL`: `https://legalease-backend.onrender.com`

4. **Deploy**
   - Click "Create Static Site"
   - Wait for deployment (3-5 minutes)

### Step 4: Update CORS Settings

After both services are deployed, update your backend's CORS settings:

1. Go to your backend service in Render
2. Add environment variable:
   - `FRONTEND_URL`: `https://your-frontend-url.onrender.com`

## 🔧 Configuration Files Created

- `build.sh` - Build script for Django
- `render.yaml` - Render configuration (optional)
- `frontend/.env.production` - Production environment variables

## 🌐 Access Your Application

After deployment:
- **Frontend**: `https://legalease-frontend.onrender.com`
- **Backend API**: `https://legalease-backend.onrender.com`
- **Admin Panel**: `https://legalease-backend.onrender.com/admin`

## 🔍 Troubleshooting

### Common Issues:

1. **Build Fails**
   - Check build logs in Render dashboard
   - Ensure all dependencies are in requirements.txt
   - Verify Python version compatibility

2. **CORS Errors**
   - Update ALLOWED_HOSTS in settings.py
   - Add frontend URL to CORS_ALLOWED_ORIGINS

3. **Static Files Not Loading**
   - Ensure WhiteNoise is configured
   - Check STATIC_ROOT setting

4. **API Connection Issues**
   - Verify REACT_APP_API_URL in frontend
   - Check backend service is running

### Logs and Debugging:
- View logs in Render dashboard
- Use Django admin for backend debugging
- Check browser console for frontend errors

## 💰 Free Tier Limits

**Render Free Tier includes:**
- 750 hours/month for web services
- Automatic sleep after 15 minutes of inactivity
- 500MB RAM per service
- Unlimited static sites

## 🔄 Updates and Redeployment

To update your application:
1. Push changes to GitHub
2. Render will automatically redeploy
3. Or manually trigger deployment in dashboard

## 📞 Support

If you encounter issues:
1. Check Render documentation
2. Review deployment logs
3. Verify environment variables
4. Test locally first

Your LegalEase application should now be live and accessible worldwide! 🎉