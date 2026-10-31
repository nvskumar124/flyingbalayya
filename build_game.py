import json, os

assets_path = r'C:\Users\VINAY\Downloads\balgame\assets\assets_pro.json'
with open(assets_path, 'r') as f:
    assets = json.load(f)

html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Monetag Push Notification Tag (Zone: 12162169) - Placed immediately after <head> as requested by Monetag -->
  <script src="https://5gvci.com/act/files/tag.min.js?z=12162169" data-cfasync="false" async></script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Flying Balayya - Balayya Babu Game</title>
  
  <!-- ============================================================
       MONETAG INTEGRATION (NON-INTRUSIVE)
       ============================================================ -->
  <!-- 1. Verification Meta Tag -->
  <meta name="monetag" content="bdb1524c9dd767d320f624d86bbe9a4a">

  <!-- 2. Banner / In-Page Push (Zone: 12162167) -->
  <script>(function(s){s.dataset.zone='12162167',s.src='https://nap5k.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bungee&family=Rubik+Mono+One&family=Teko:wght@700&family=Yatra+One&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --primary-gold: #fbbf24;
      --glow-gold: #f59e0b;
      --accent-red: #ef4444;
      --neon-cyan: #38bdf8;
      --bg-dark: #030712;
      --card-bg: rgba(13, 20, 38, 0.94);
    }
    * {
      box-sizing: border-box;
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;
      margin: 0;
      padding: 0;
    }
    body, html {
      width: 100%;
      height: 100%;
      overflow: hidden;
      background: radial-gradient(circle at 50% 30%, #111c38 0%, #060b18 60%, #020409 100%);
      font-family: 'Bungee', cursive, sans-serif;
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    /* Overall Layout: Left Side Ad + Game + Right Side Ad */
    #page-layout {
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 20px;
      padding: 10px;
      overflow: hidden;
    }

    /* SIDE AD PANELS (DESKTOP & TABLETS - ZERO GAMEPLAY INTERRUPTION) */
    .side-ad-panel {
      width: 160px;
      height: 600px;
      max-height: 90vh;
      background: linear-gradient(180deg, rgba(15, 23, 42, 0.92) 0%, rgba(10, 15, 30, 0.96) 100%);
      border: 2px solid rgba(251, 191, 36, 0.35);
      border-radius: 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 12px 8px;
      box-shadow: 0 0 25px rgba(0, 0, 0, 0.6), 0 0 15px rgba(251, 191, 36, 0.2);
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .side-ad-badge {
      font-size: 9px;
      color: #94a3b8;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      background: rgba(0, 0, 0, 0.6);
      padding: 3px 8px;
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .side-ad-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 14px;
      text-align: center;
      color: #ffd700;
      font-size: 11px;
      line-height: 1.4;
      cursor: pointer;
      text-decoration: none;
      padding: 10px 4px;
      width: 100%;
      border-radius: 12px;
      transition: all 0.2s;
    }
    .side-ad-content:hover {
      background: rgba(251, 191, 36, 0.1);
      transform: scale(1.02);
    }
    .side-ad-icon {
      font-size: 38px;
      filter: drop-shadow(0 0 10px rgba(251, 191, 36, 0.6));
    }
    .side-ad-cta {
      background: linear-gradient(135deg, #f59e0b, #ea580c);
      color: #fff;
      padding: 8px 12px;
      border-radius: 20px;
      font-size: 10px;
      letter-spacing: 1px;
      box-shadow: 0 4px 12px rgba(245, 158, 11, 0.4);
    }

    /* Hide side ads on mobile so game has 100% full screen */
    @media (max-width: 820px) {
      .side-ad-panel {
        display: none !important;
      }
      #page-layout {
        padding: 0;
        gap: 0;
      }
    }

    /* Main Game Container */
    #game-container {
      position: relative;
      z-index: 20;
      width: 100%;
      max-width: 440px;
      height: 100%;
      max-height: 850px;
      overflow: hidden;
      background: #000;
      box-shadow: 0 0 60px rgba(245, 158, 11, 0.3), 0 0 120px rgba(56, 189, 248, 0.2);
      border-radius: 24px;
      border: 3px solid rgba(251, 191, 36, 0.35);
    }
    @media (max-width: 480px) {
      #game-container {
        max-width: 100%;
        max-height: 100%;
        border-radius: 0;
        border: none;
      }
    }
    canvas {
      display: block;
      width: 100%;
      height: 100%;
    }
    /* Top Bar HUD */
    .top-bar {
      position: absolute;
      top: 14px;
      left: 14px;
      right: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      pointer-events: none;
      z-index: 20;
    }
    .score-display {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      font-size: 54px;
      font-family: 'Rubik Mono One', 'Bungee', sans-serif;
      color: #ffffff;
      text-shadow: 0 4px 0 #000, 0 0 20px rgba(251, 191, 36, 0.9), -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000;
      transition: transform 0.12s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .score-pop {
      transform: translateX(-50%) scale(1.35) rotate(-3deg);
      color: #ffd700;
    }
    .hud-controls {
      display: flex;
      gap: 10px;
      pointer-events: auto;
    }
    .icon-btn {
      background: rgba(15, 23, 42, 0.75);
      border: 2px solid rgba(251, 191, 36, 0.4);
      backdrop-filter: blur(10px);
      width: 42px;
      height: 42px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      cursor: pointer;
      font-size: 18px;
      transition: all 0.2s;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    }
    .icon-btn:hover {
      transform: scale(1.1);
      border-color: #ffd700;
      box-shadow: 0 0 18px rgba(251, 191, 36, 0.8);
    }
    .icon-btn:active {
      transform: scale(0.95);
    }

    /* Subtitle banner for Audio 3 (Intro) */
    #introSubtitleBanner {
      position: absolute;
      bottom: 25px;
      left: 16px;
      right: 16px;
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 27, 75, 0.95));
      border: 2px solid rgba(251, 191, 36, 0.8);
      border-radius: 14px;
      padding: 10px 16px;
      text-align: center;
      z-index: 25;
      box-shadow: 0 0 25px rgba(245, 158, 11, 0.5);
      animation: bannerSlideUp 0.4s ease-out;
      display: none;
    }
    @keyframes bannerSlideUp {
      from { transform: translateY(30px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    .subtitle-speaker {
      font-size: 10px;
      color: #ffd700;
      letter-spacing: 1.5px;
      margin-bottom: 2px;
    }
    .subtitle-quote {
      font-family: 'Teko', sans-serif;
      font-size: 18px;
      color: #ffffff;
      line-height: 1.1;
      letter-spacing: 1px;
    }

    /* Start Screen Overlay */
    #start-overlay {
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at center, rgba(17, 24, 39, 0.9) 0%, rgba(3, 7, 18, 0.97) 100%);
      backdrop-filter: blur(8px);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 30;
      gap: 14px;
      text-align: center;
      padding: 18px;
    }
    .logo-badge {
      position: relative;
      width: 100px;
      height: 100px;
      border-radius: 50%;
      border: 3px solid #ffd700;
      box-shadow: 0 0 35px rgba(251, 191, 36, 0.8), inset 0 0 20px rgba(251, 191, 36, 0.5);
      overflow: hidden;
      animation: floatBadge 3s ease-in-out infinite alternate;
    }
    @keyframes floatBadge {
      0% { transform: translateY(0) rotate(-2deg); }
      100% { transform: translateY(-8px) rotate(2deg); }
    }
    .logo-badge img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .title-banner {
      font-family: 'Rubik Mono One', 'Bungee', sans-serif;
      font-size: 30px;
      line-height: 1.05;
      background: linear-gradient(180deg, #ffffff 0%, #ffd700 45%, #ea580c 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 6px 15px rgba(245, 158, 11, 0.7));
      text-transform: uppercase;
      letter-spacing: 1.5px;
    }
    .subtitle-telugu {
      font-family: 'Yatra One', cursive;
      font-size: 19px;
      color: #38bdf8;
      text-shadow: 0 0 15px rgba(56, 189, 248, 0.9);
      margin-top: -4px;
    }
    .enter-game-btn {
      background: linear-gradient(135deg, #f59e0b 0%, #ea580c 50%, #b91c1c 100%);
      border: 2px solid #ffd700;
      color: #ffffff;
      font-family: 'Bungee', sans-serif;
      font-size: 15px;
      letter-spacing: 1.5px;
      padding: 14px 30px;
      border-radius: 30px;
      cursor: pointer;
      box-shadow: 0 0 30px rgba(245, 158, 11, 0.8), 0 8px 25px rgba(0, 0, 0, 0.5);
      animation: enterPulse 1.2s infinite alternate;
      transition: all 0.2s;
    }
    @keyframes enterPulse {
      0% { transform: scale(0.97); box-shadow: 0 0 20px rgba(245, 158, 11, 0.6); }
      100% { transform: scale(1.05); box-shadow: 0 0 40px rgba(251, 191, 36, 1), 0 0 15px #fff; }
    }
    .instructions-mini {
      font-size: 11px;
      color: #cbd5e1;
      line-height: 1.4;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 12px;
      padding: 8px 14px;
      max-width: 290px;
    }

    /* DISCLAIMER BANNER */
    .disclaimer-banner {
      font-family: sans-serif;
      font-size: 9.5px;
      line-height: 1.35;
      color: #94a3b8;
      background: rgba(0, 0, 0, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 8px;
      padding: 6px 10px;
      max-width: 320px;
      text-align: center;
    }
    .disclaimer-banner strong {
      color: #ffd700;
    }

    /* GAME OVER MODAL (CLEAN & UNINTERRUPTED) */
    #gameover-overlay {
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.84);
      backdrop-filter: blur(10px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 50;
      padding: 14px;
    }
    .modal-container {
      position: relative;
      width: 100%;
      max-width: 310px;
      background: linear-gradient(180deg, rgba(26, 32, 53, 0.98) 0%, rgba(11, 16, 29, 0.99) 100%);
      border: 2px solid rgba(239, 68, 68, 0.6);
      border-radius: 20px;
      padding: 18px 16px 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      box-shadow: 0 0 50px rgba(239, 68, 68, 0.6), 0 0 90px rgba(245, 158, 11, 0.3), inset 0 1px 1px rgba(255, 255, 255, 0.25);
      animation: modalPop 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    @keyframes modalPop {
      0% { transform: scale(0.7) translateY(40px); opacity: 0; }
      100% { transform: scale(1) translateY(0); opacity: 1; }
    }
    .failed-title {
      font-family: 'Teko', sans-serif;
      font-size: 42px;
      line-height: 0.9;
      color: #ff3333;
      text-transform: uppercase;
      letter-spacing: 2px;
      text-shadow: 0 0 20px rgba(255, 51, 51, 0.9), 0 2px 0 #000;
    }
    .failed-dialogue {
      font-family: 'Yatra One', cursive;
      font-size: 13px;
      color: #fee2e2;
      text-align: center;
      line-height: 1.35;
      background: rgba(239, 68, 68, 0.15);
      padding: 6px 10px;
      border-radius: 8px;
      border: 1px solid rgba(239, 68, 68, 0.4);
    }
    .balayya-card-wrapper {
      position: relative;
      width: 254px;
      height: 142px;
      border-radius: 14px;
      overflow: hidden;
      border: 2.5px solid #ef4444;
      box-shadow: 0 0 35px rgba(239, 68, 68, 0.9), 0 0 15px rgba(251, 191, 36, 0.6);
      background: #000;
    }
    .balayya-card-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .score-summary-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      width: 100%;
      background: rgba(10, 15, 26, 0.8);
      border-radius: 12px;
      padding: 8px 12px;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .score-item {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .score-item-label {
      font-size: 9px;
      color: #94a3b8;
      letter-spacing: 1px;
    }
    .score-item-value {
      font-family: 'Rubik Mono One', monospace;
      font-size: 24px;
      color: #38bdf8;
      text-shadow: 0 0 10px rgba(56, 189, 248, 0.6);
    }
    .score-item-value.gold {
      color: #ffd700;
      text-shadow: 0 0 12px rgba(255, 215, 0, 0.8);
    }

    .play-again-btn {
      width: 100%;
      padding: 13px;
      background: linear-gradient(180deg, #2563eb 0%, #1d4ed8 100%);
      border: none;
      border-radius: 12px;
      color: #fff;
      font-family: 'Bungee', sans-serif;
      font-size: 15px;
      letter-spacing: 1.5px;
      cursor: pointer;
      box-shadow: 0 6px 25px rgba(37, 99, 235, 0.6), inset 0 1px 1px rgba(255, 255, 255, 0.4);
      transition: all 0.15s;
    }
    .play-again-btn:hover {
      background: linear-gradient(180deg, #3b82f6 0%, #2563eb 100%);
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(59, 130, 246, 0.8);
    }
    .play-again-btn:active {
      transform: translateY(1px);
    }
    .modal-disclaimer-note {
      font-family: sans-serif;
      font-size: 8px;
      color: #64748b;
      text-align: center;
      line-height: 1.3;
    }
    /* Red screen flash on death */
    .red-flash {
      position: absolute;
      inset: 0;
      background: rgba(239, 68, 68, 0.45);
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.1s;
      z-index: 40;
    }
    /* Screen shake */
    .screen-shake {
      animation: shake 0.35s cubic-bezier(.36,.07,.19,.97) both;
    }
    @keyframes shake {
      10%, 90% { transform: translate3d(-4px, 0, 0); }
      20%, 80% { transform: translate3d(5px, -3px, 0); }
      30%, 50%, 70% { transform: translate3d(-6px, 5px, 0); }
      40%, 60% { transform: translate3d(6px, -5px, 0); }
    }
    /* Floating toasts */
    .floating-toast {
      position: absolute;
      left: 50%;
      top: 28%;
      transform: translate(-50%, -50%);
      font-family: 'Rubik Mono One', sans-serif;
      font-size: 26px;
      color: #ffd700;
      text-shadow: 0 3px 0 #000, 0 0 25px #f59e0b;
      pointer-events: none;
      z-index: 35;
      animation: floatUpFade 0.9s forwards ease-out;
    }
    @keyframes floatUpFade {
      0% { transform: translate(-50%, 0) scale(0.5); opacity: 0; }
      25% { transform: translate(-50%, -15px) scale(1.2); opacity: 1; }
      100% { transform: translate(-50%, -60px) scale(1); opacity: 0; }
    }
  </style>
</head>
<body>
  <!-- Monetag In-Page Push / Banner Ads (Zone: 12162167) -->
  <script>(function(s){s.dataset.zone='12162167',s.src='https://nap5k.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>

<div id="page-layout">
  <!-- ==============================================
       LEFT SIDE AD (160x600 Skyscraper - On sides only!)
       ============================================== -->
  <aside class="side-ad-panel" id="leftSideAd">
    <span class="side-ad-badge">Sponsored</span>
    
    <a class="side-ad-content" id="leftAdLink" href="https://uplcm.com/4/12162165" target="_blank" rel="noopener">
      <div class="side-ad-icon">🦁</div>
      <div style="font-weight:bold; font-size:13px; color:#fff;">JAI BALAYYA</div>
      <div style="font-size:10px; color:#94a3b8;">Trending Mobile Games &amp; Entertainment</div>
      <div class="side-ad-cta">EXPLORE NOW</div>
    </a>

    <span style="font-size:8px; color:#64748b; letter-spacing:1px;">MONETAG ADS</span>
  </aside>

  <!-- ==============================================
       MAIN GAME CONTAINER (Center - Completely Uninterrupted)
       ============================================== -->
  <main id="game-container">
    <canvas id="gameCanvas"></canvas>
    <div id="redFlash" class="red-flash"></div>

    <!-- Top Bar HUD -->
    <div class="top-bar">
      <div class="hud-controls">
        <button id="soundBtn" class="icon-btn" title="Toggle Sound">🔊</button>
      </div>
      <div id="scoreDisplay" class="score-display">0</div>
      <div class="hud-controls">
        <button id="skinBtn" class="icon-btn" title="Toggle Avatar Skin">🕶️</button>
      </div>
    </div>

    <!-- Audio 3 Intro Subtitle Banner -->
    <div id="introSubtitleBanner">
      <div class="subtitle-speaker">🦁 NANDAMURI BALAKRISHNA</div>
      <div class="subtitle-quote">"Don't trouble the trouble! If you trouble the trouble, trouble troubles you! I am not the trouble, I am the TRUTH!"</div>
    </div>

    <!-- Start Screen Overlay ("Enter the Game") -->
    <div id="start-overlay">
      <div class="logo-badge">
        <img id="startBadgeImg" alt="Balayya Medallion">
      </div>
      <div>
        <div class="title-banner">FLYING BALAYYA</div>
        <div class="subtitle-telugu">బాలయ్య బాబు గేమ్</div>
      </div>
      
      <button id="enterGameBtn" class="enter-game-btn">🦁 ENTER THE GAME 🦁</button>

      <div class="instructions-mini">
        <p style="color:#ffd700; font-weight:bold; margin-bottom:2px;">🎮 HOW TO PLAY:</p>
        <p>• <strong>TAP SCREEN / SPACEBAR</strong> to flap &amp; fly</p>
        <p>• Dodge the Mansion House Whiskey bottles!</p>
      </div>

      <!-- ENTERTAINMENT & REMOVAL DISCLAIMER -->
      <div class="disclaimer-banner">
        ⚠️ <strong>Notice:</strong> This game is created purely for entertainment &amp; fan-made parody purposes. We have immense respect for Nandamuri Balakrishna garu and all respective copyright holders. If any content violates any copyright or policy, please contact us and it will be removed immediately.
      </div>
    </div>

    <!-- Game Over Modal (Clean, No annoying popups) -->
    <div id="gameover-overlay">
      <div class="modal-container">
        <div class="failed-title">YOU FAILED!</div>
        <div class="failed-dialogue">Sorry, ఇలా మాట్లాడకూడదు...<br>ల*** కొడక గుద్దలూడదీసి కొడతా!</div>
        
        <div class="balayya-card-wrapper">
          <img id="modalCardImg" class="balayya-card-img" alt="Balayya Furious Warning">
        </div>

        <div class="score-summary-grid">
          <div class="score-item">
            <span class="score-item-label">SCORE</span>
            <span id="finalScore" class="score-item-value">0</span>
          </div>
          <div class="score-item">
            <span class="score-item-label">BEST</span>
            <span id="bestScore" class="score-item-value gold">0</span>
          </div>
        </div>

        <button id="playAgainBtn" class="play-again-btn">PLAY AGAIN</button>

        <div class="modal-disclaimer-note">
          Fan-made parody for entertainment purposes only. All copyrights belong to their respective owners.
        </div>
      </div>
    </div>
  </main>

  <!-- ==============================================
       RIGHT SIDE AD (160x600 Skyscraper - On sides only!)
       ============================================== -->
  <aside class="side-ad-panel" id="rightSideAd">
    <span class="side-ad-badge">Sponsored</span>
    
    <a class="side-ad-content" id="rightAdLink" href="https://uplcm.com/4/12162165" target="_blank" rel="noopener">
      <div class="side-ad-icon">⚡</div>
      <div style="font-weight:bold; font-size:13px; color:#fff;">HOT REWARDS</div>
      <div style="font-size:10px; color:#94a3b8;">Discover Top Deals &amp; Special Offers</div>
      <div class="side-ad-cta">CHECK IT OUT</div>
    </a>

    <span style="font-size:8px; color:#64748b; letter-spacing:1px;">MONETAG ADS</span>
  </aside>
</div>

<script>
// ============================================================
// MONETAG SIDE ADS CONFIGURATION
// You can set your Monetag Direct Link URL for the side banners:
// ============================================================
const MONETAG_CONFIG = {
  directLinkUrl: 'https://uplcm.com/4/12162165'
};

function handleSideAdClick(e) {
  e.preventDefault();
  if (MONETAG_CONFIG.directLinkUrl) {
    window.open(MONETAG_CONFIG.directLinkUrl, '_blank');
  } else {
    window.open('https://api.whatsapp.com/send?text=Play%20the%20viral%20Flying%20Balayya%20Game!%20Jai%20Balayya!', '_blank');
  }
}

document.getElementById('leftAdLink').addEventListener('click', handleSideAdClick);
document.getElementById('rightAdLink').addEventListener('click', handleSideAdClick);

// --- EMBEDDED ASSETS (STRICTLY 3 AUDIOS + HIGH RES GRAPHICS) ---
const ASSETS = ''' + json.dumps(assets) + ''';

// --- STRICT 3-AUDIO SYSTEM ---
class BalayyaAudioManager {
  constructor() {
    this.soundEnabled = true;

    // 1. Audio 1: When death ("Sorry ila matladakoodadu... Lanja kodaka! Guddaloodadeesi kodatha!")
    this.audioDeath = new Audio(ASSETS.audio_death);
    this.audioDeath.preload = 'auto';

    // 2. Audio 2: While playing ("Nee kanti choopulloki na pranam cherinde...")
    this.audioGameplay = new Audio(ASSETS.audio_gameplay);
    this.audioGameplay.preload = 'auto';
    this.audioGameplay.loop = true;
    this.audioGameplay.volume = 0.75;

    // 3. Audio 3: After entering the game ("Don't trouble the trouble... I am the truth!")
    this.audioIntro = new Audio(ASSETS.audio_intro);
    this.audioIntro.preload = 'auto';
    this.audioIntro.volume = 1.0;

    // Chain: when Audio 3 finishes, smoothly start Audio 2 if still in game
    this.audioIntro.onended = () => {
      document.getElementById('introSubtitleBanner').style.display = 'none';
      if (this.soundEnabled && (gameState === 'PLAYING' || gameState === 'HOVER')) {
        this.playGameplayAudio();
      }
    };
  }

  // 3. AFTER ENTERING THE GAME
  playIntroAudio() {
    if (!this.soundEnabled) return;
    this.stopAll();
    this.audioIntro.currentTime = 0;
    this.audioIntro.play().catch(e => console.log('Audio 3 waiting for user gesture'));
    document.getElementById('introSubtitleBanner').style.display = 'block';
  }

  // 2. WHILE PLAYING
  playGameplayAudio() {
    if (!this.soundEnabled) return;
    this.audioIntro.pause();
    this.audioDeath.pause();
    document.getElementById('introSubtitleBanner').style.display = 'none';
    this.audioGameplay.currentTime = 0;
    this.audioGameplay.play().catch(e => console.log('Audio 2 play error', e));
  }

  // 1. WHEN DEATH
  playDeathAudio() {
    if (!this.soundEnabled) return;
    this.audioGameplay.pause();
    this.audioIntro.pause();
    document.getElementById('introSubtitleBanner').style.display = 'none';
    this.audioDeath.currentTime = 0;
    this.audioDeath.play().catch(e => console.log('Audio 1 play error', e));
  }

  stopAll() {
    this.audioDeath.pause();
    this.audioGameplay.pause();
    this.audioIntro.pause();
  }

  toggleMute() {
    this.soundEnabled = !this.soundEnabled;
    if (!this.soundEnabled) {
      this.stopAll();
    } else {
      if (gameState === 'PLAYING') {
        this.playGameplayAudio();
      }
    }
    return this.soundEnabled;
  }
}

const audioManager = new BalayyaAudioManager();

// --- IMAGE LOADER ---
const images = {};
function loadImages(onComplete) {
  let loaded = 0;
  const keys = ['player_avatar', 'player_shades', 'modal_card', 'mansion_bottle'];
  keys.forEach(k => {
    const img = new Image();
    img.src = ASSETS[k];
    img.onload = () => {
      images[k] = img;
      loaded++;
      if (loaded === keys.length) onComplete();
    };
    img.onerror = () => {
      console.warn('Could not load image', k);
      loaded++;
      if (loaded === keys.length) onComplete();
    };
  });
}

// --- GAME LOGIC ---
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const redFlash = document.getElementById('redFlash');
const scoreDisplay = document.getElementById('scoreDisplay');
const startOverlay = document.getElementById('start-overlay');
const gameoverOverlay = document.getElementById('gameover-overlay');
const startBadgeImg = document.getElementById('startBadgeImg');
const modalCardImg = document.getElementById('modalCardImg');
const finalScoreEl = document.getElementById('finalScore');
const bestScoreEl = document.getElementById('bestScore');
const enterGameBtn = document.getElementById('enterGameBtn');
const playAgainBtn = document.getElementById('playAgainBtn');
const soundBtn = document.getElementById('soundBtn');
const skinBtn = document.getElementById('skinBtn');
const gameContainer = document.getElementById('game-container');

// Canvas responsive sizing
let width, height;
function resizeCanvas() {
  const rect = gameContainer.getBoundingClientRect();
  width = rect.width;
  height = rect.height;
  canvas.width = width;
  canvas.height = height;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

// Game State: 'START', 'HOVER', 'PLAYING', 'GAMEOVER'
let gameState = 'START';
let currentSkin = 'CLASSIC'; // 'CLASSIC' or 'SHADES'
let score = 0;
let bestScore = parseInt(localStorage.getItem('balayya_best_score') || '0', 10);
let frameCount = 0;

// Player Object
const player = {
  x: 80,
  y: 350,
  size: 52, // Head medallion size
  vy: 0,
  gravity: 0.38,
  jumpStrength: -7.6,
  rotation: 0,
  jetParticles: [],
  shockwaves: [],
  reset() {
    this.x = 80;
    this.y = height * 0.45;
    this.vy = 0;
    this.rotation = 0;
    this.jetParticles = [];
    this.shockwaves = [];
  },
  flap() {
    this.vy = this.jumpStrength;

    // Shockwave ring
    this.shockwaves.push({
      x: this.x,
      y: this.y,
      radius: 12,
      maxRadius: 70,
      alpha: 1.0,
      color: '#ffd700'
    });
  }
};

// Obstacle (Mansion House Bottles)
let obstacles = [];
const OBSTACLE_WIDTH = 62;
const GAP_SIZE = 162;
const SPAWN_INTERVAL = 138;

function spawnObstacle() {
  const minTop = 70;
  const maxTop = height - GAP_SIZE - 120;
  const topHeight = Math.floor(Math.random() * (maxTop - minTop)) + minTop;

  obstacles.push({
    x: width + 20,
    topHeight: topHeight,
    bottomY: topHeight + GAP_SIZE,
    width: OBSTACLE_WIDTH,
    passed: false
  });
}

// Particle system for glass shards
let particles = [];
function createBottleShatter(x, y, count = 30) {
  triggerScreenShake(14);
  for (let i = 0; i < count; i++) {
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 9 + 2;
    particles.push({
      x: x,
      y: y,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed - 2.5,
      size: Math.random() * 6 + 3,
      color: Math.random() > 0.3 ? '#fca311' : '#38bdf8',
      alpha: 1.0,
      decay: Math.random() * 0.03 + 0.018,
      rotation: Math.random() * Math.PI * 2,
      vRot: (Math.random() - 0.5) * 0.4
    });
  }
}

function showToast(text) {
  const div = document.createElement('div');
  div.className = 'floating-toast';
  div.innerText = text;
  gameContainer.appendChild(div);
  setTimeout(() => div.remove(), 900);
}

function triggerScreenShake(frames = 10) {
  gameContainer.classList.add('screen-shake');
  setTimeout(() => {
    gameContainer.classList.remove('screen-shake');
  }, frames * 25);
}

function updateScoreUI() {
  scoreDisplay.innerText = score;
  scoreDisplay.classList.add('score-pop');
  setTimeout(() => scoreDisplay.classList.remove('score-pop'), 120);

  if (score > bestScore) {
    bestScore = score;
    localStorage.setItem('balayya_best_score', bestScore);
  }

  if (score > 0 && score % 5 === 0) {
    const compliments = ['MASS!', 'SIMHAM!', 'RECORD-U!', 'JAI BALAYYA!', 'ROAR!'];
    showToast(compliments[(score / 5 - 1) % compliments.length]);
  }
}

// --- HIGH-END BACKGROUND GRAPHICS ---
const stars = Array.from({length: 50}, () => ({
  x: Math.random() * 440,
  y: Math.random() * 420,
  size: Math.random() * 2.2 + 0.8,
  blinkSpeed: Math.random() * 0.05 + 0.02,
  alpha: Math.random()
}));

const embers = Array.from({length: 25}, () => ({
  x: Math.random() * 440,
  y: Math.random() * 800,
  vx: (Math.random() - 0.5) * 0.6,
  vy: -Math.random() * 1.2 - 0.4,
  size: Math.random() * 3 + 1.5,
  alpha: Math.random() * 0.7 + 0.3
}));

function drawBackground() {
  // 1. Deep Midnight Cosmic Sky
  const grad = ctx.createLinearGradient(0, 0, 0, height);
  grad.addColorStop(0, '#030712');
  grad.addColorStop(0.35, '#0b1329');
  grad.addColorStop(0.7, '#151d3b');
  grad.addColorStop(1, '#020409');
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, width, height);

  // 2. Golden Moon with Balayya Lion Glow in upper right
  const moonX = width - 75;
  const moonY = 85;
  const moonRadius = 38;

  // Moon Outer Glow
  const moonGlow = ctx.createRadialGradient(moonX, moonY, moonRadius * 0.4, moonX, moonY, moonRadius * 2.5);
  moonGlow.addColorStop(0, 'rgba(251, 191, 36, 0.4)');
  moonGlow.addColorStop(0.5, 'rgba(245, 158, 11, 0.15)');
  moonGlow.addColorStop(1, 'rgba(245, 158, 11, 0)');
  ctx.fillStyle = moonGlow;
  ctx.beginPath();
  ctx.arc(moonX, moonY, moonRadius * 2.5, 0, Math.PI * 2);
  ctx.fill();

  // Moon Orb
  const moonBody = ctx.createRadialGradient(moonX - 8, moonY - 8, 5, moonX, moonY, moonRadius);
  moonBody.addColorStop(0, '#fffbeb');
  moonBody.addColorStop(0.7, '#fef08a');
  moonBody.addColorStop(1, '#facc15');
  ctx.fillStyle = moonBody;
  ctx.beginPath();
  ctx.arc(moonX, moonY, moonRadius, 0, Math.PI * 2);
  ctx.fill();

  // Subtle craters
  ctx.fillStyle = 'rgba(217, 119, 6, 0.2)';
  ctx.beginPath();
  ctx.arc(moonX - 10, moonY + 8, 9, 0, Math.PI * 2);
  ctx.arc(moonX + 12, moonY - 12, 6, 0, Math.PI * 2);
  ctx.arc(moonX + 8, moonY + 14, 8, 0, Math.PI * 2);
  ctx.fill();

  // 3. Animated Hollywood/Tollywood Premiere Searchlights
  const t = frameCount * 0.015;
  const light1Angle = Math.sin(t) * 0.35 - 0.2;
  const light2Angle = Math.cos(t * 0.9) * 0.35 + 0.2;

  drawSearchlight(width * 0.25, height - 38, light1Angle, 'rgba(251, 191, 36, 0.12)');
  drawSearchlight(width * 0.75, height - 38, light2Angle, 'rgba(56, 189, 248, 0.12)');

  // 4. Twinkling Stars
  stars.forEach(s => {
    s.alpha += s.blinkSpeed;
    const a = (Math.sin(s.alpha) + 1) / 2;
    ctx.fillStyle = `rgba(255, 255, 255, ${a * 0.85})`;
    ctx.beginPath();
    ctx.arc((s.x % width), s.y, s.size, 0, Math.PI * 2);
    ctx.fill();
  });

  // 5. Floating Golden Embers
  embers.forEach(e => {
    e.x += e.vx;
    e.y += e.vy;
    if (e.y < -10) {
      e.y = height + 10;
      e.x = Math.random() * width;
    }
    ctx.fillStyle = `rgba(251, 191, 36, ${e.alpha})`;
    ctx.beginPath();
    ctx.arc((e.x + width) % width, e.y, e.size, 0, Math.PI * 2);
    ctx.fill();
  });

  // 6. City Skyline Silhouette
  ctx.fillStyle = '#060d1f';
  const bldgWidth = 34;
  const numBldgs = Math.ceil(width / bldgWidth) + 1;
  for (let i = 0; i < numBldgs; i++) {
    const h = ((i * 43) % 110) + 75;
    ctx.fillRect(i * bldgWidth, height - h - 38, bldgWidth - 2, h);

    // Glowing Neon Windows
    ctx.fillStyle = (i % 2 === 0) ? 'rgba(251, 191, 36, 0.45)' : 'rgba(56, 189, 248, 0.45)';
    for (let r = 0; r < 5; r++) {
      if ((i + r) % 3 !== 0) {
        ctx.fillRect(i * bldgWidth + 5, height - h - 28 + r * 15, 5, 6);
        ctx.fillRect(i * bldgWidth + 18, height - h - 28 + r * 15, 5, 6);
      }
    }
    // Red beacon light on antenna
    if (i % 3 === 0) {
      ctx.fillStyle = Math.sin(frameCount * 0.1 + i) > 0 ? '#ef4444' : '#7f1d1d';
      ctx.beginPath();
      ctx.arc(i * bldgWidth + 15, height - h - 45, 2.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(i * bldgWidth + 15, height - h - 38);
      ctx.lineTo(i * bldgWidth + 15, height - h - 44);
      ctx.stroke();
    }
    ctx.fillStyle = '#060d1f';
  }

  // 7. Ground / Highway Strip
  const groundGrad = ctx.createLinearGradient(0, height - 38, 0, height);
  groundGrad.addColorStop(0, '#1e293b');
  groundGrad.addColorStop(0.3, '#0f172a');
  groundGrad.addColorStop(1, '#020617');
  ctx.fillStyle = groundGrad;
  ctx.fillRect(0, height - 38, width, 38);

  // Gold Cyber Rim Line
  ctx.strokeStyle = '#f59e0b';
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(0, height - 38);
  ctx.lineTo(width, height - 38);
  ctx.stroke();

  // Scrolling Golden Mass Marquee
  ctx.font = '11px Bungee';
  ctx.fillStyle = 'rgba(251, 191, 36, 0.6)';
  ctx.fillText('★ JAI BALAYYA ★ GOD OF MASSES ★ NANDAMURI BALAKRISHNA ★', ((frameCount * -1.8) % 380), height - 14);
}

function drawSearchlight(x, y, angle, color) {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(angle);

  const grad = ctx.createLinearGradient(0, 0, 0, -height);
  grad.addColorStop(0, color);
  grad.addColorStop(1, 'rgba(255, 255, 255, 0)');

  ctx.fillStyle = grad;
  ctx.beginPath();
  ctx.moveTo(-10, 0);
  ctx.lineTo(10, 0);
  ctx.lineTo(90, -height);
  ctx.lineTo(-90, -height);
  ctx.closePath();
  ctx.fill();

  ctx.restore();
}

// Draw Mansion House bottle
function drawBottle(x, y, w, h, isInverted = false) {
  const bottleImg = images.mansion_bottle;
  ctx.save();
  ctx.translate(x + w / 2, y + h / 2);
  if (isInverted) {
    ctx.scale(1, -1);
  }
  if (bottleImg && bottleImg.complete) {
    ctx.drawImage(bottleImg, -w / 2, -h / 2, w, h);
  } else {
    ctx.fillStyle = '#d97706';
    ctx.fillRect(-w/2, -h/2, w, h);
  }
  ctx.restore();
}

// Draw Player (Balayya Medallion)
function drawPlayer() {
  // 1. Draw Exhaust Flame & Spark Particles
  player.jetParticles.forEach(p => {
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
    ctx.fillStyle = p.color;
    ctx.globalAlpha = p.alpha;
    ctx.fill();
    ctx.globalAlpha = 1.0;
  });

  // 2. Draw Shockwaves
  player.shockwaves.forEach(sw => {
    ctx.save();
    ctx.beginPath();
    ctx.arc(sw.x, sw.y, sw.radius, 0, Math.PI * 2);
    ctx.strokeStyle = sw.color;
    ctx.lineWidth = 3.5;
    ctx.globalAlpha = sw.alpha;
    ctx.shadowColor = '#ffd700';
    ctx.shadowBlur = 12;
    ctx.stroke();
    ctx.restore();
  });

  // 3. Draw Balayya Medallion
  ctx.save();
  ctx.translate(player.x, player.y);
  ctx.rotate(player.rotation);

  // Outer Golden Aura Pulse
  const auraPulse = Math.sin(frameCount * 0.15) * 4;
  ctx.beginPath();
  ctx.arc(0, 0, player.size / 2 + 4 + auraPulse, 0, Math.PI * 2);
  ctx.fillStyle = 'rgba(251, 191, 36, 0.25)';
  ctx.fill();

  // Head Sprite
  const headImg = (currentSkin === 'SHADES') ? images.player_shades : images.player_avatar;
  if (headImg && headImg.complete) {
    ctx.drawImage(headImg, -player.size / 2, -player.size / 2, player.size, player.size);
  } else {
    ctx.fillStyle = '#fef08a';
    ctx.beginPath();
    ctx.arc(0, 0, player.size / 2, 0, Math.PI * 2);
    ctx.fill();
  }

  // Dual Mini Thruster Nozzles at base
  ctx.fillStyle = '#475569';
  ctx.fillRect(-10, player.size / 2 - 3, 7, 5);
  ctx.fillRect(3, player.size / 2 - 3, 7, 5);

  ctx.restore();
}

function drawObstacles() {
  obstacles.forEach(obs => {
    // Top bottle (hanging down)
    drawBottle(obs.x, 0, obs.width, obs.topHeight, true);
    // Bottom bottle (standing upright)
    drawBottle(obs.x, obs.bottomY, obs.width, height - obs.bottomY - 38, false);
  });
}

function drawParticles() {
  particles.forEach(p => {
    ctx.save();
    ctx.translate(p.x, p.y);
    ctx.rotate(p.rotation);
    ctx.fillStyle = p.color;
    ctx.globalAlpha = p.alpha;
    ctx.fillRect(-p.size/2, -p.size/2, p.size, p.size);
    ctx.restore();
  });
}

// --- UPDATE LOOP ---
function update() {
  frameCount++;

  // Update Shockwaves
  for (let i = player.shockwaves.length - 1; i >= 0; i--) {
    const sw = player.shockwaves[i];
    sw.radius += 4.5;
    sw.alpha -= 0.04;
    if (sw.alpha <= 0 || sw.radius >= sw.maxRadius) {
      player.shockwaves.splice(i, 1);
    }
  }

  // Update Particles
  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;
    p.vy += 0.24;
    p.rotation += p.vRot;
    p.alpha -= p.decay;
    if (p.alpha <= 0) {
      particles.splice(i, 1);
    }
  }

  if (gameState === 'PLAYING') {
    // Physics
    player.vy += player.gravity;
    player.y += player.vy;

    // Rotation banking
    if (player.vy < 0) {
      player.rotation = -0.3;
    } else {
      player.rotation = Math.min(Math.PI / 2.7, player.rotation + 0.045);
    }

    // Spawn Jet Flame Particles
    player.jetParticles.push({
      x: player.x - Math.cos(player.rotation) * 16,
      y: player.y + player.size / 2 - 2,
      size: Math.random() * 4 + 3,
      color: Math.random() > 0.4 ? '#38bdf8' : '#f59e0b',
      alpha: 0.9,
      decay: 0.055
    });

    for (let i = player.jetParticles.length - 1; i >= 0; i--) {
      const jp = player.jetParticles[i];
      jp.x -= 3.2;
      jp.alpha -= jp.decay;
      if (jp.alpha <= 0) {
        player.jetParticles.splice(i, 1);
      }
    }

    // Spawning obstacles
    if (frameCount % SPAWN_INTERVAL === 0) {
      spawnObstacle();
    }

    // Move & Collision
    const playerRadius = player.size * 0.42;

    for (let i = obstacles.length - 1; i >= 0; i--) {
      const obs = obstacles[i];
      obs.x -= 2.7;

      // Passing score
      if (!obs.passed && obs.x + obs.width < player.x) {
        obs.passed = true;
        score++;
        updateScoreUI();
      }

      // Collision Detection
      const hitTop = (player.x + playerRadius > obs.x + 4 && 
                      player.x - playerRadius < obs.x + obs.width - 4 && 
                      player.y - playerRadius < obs.topHeight);

      const hitBottom = (player.x + playerRadius > obs.x + 4 && 
                         player.x - playerRadius < obs.x + obs.width - 4 && 
                         player.y + playerRadius > obs.bottomY);

      if (hitTop || hitBottom) {
        triggerGameOver();
        return;
      }

      if (obs.x + obs.width < -30) {
        obstacles.splice(i, 1);
      }
    }

    // Ceiling / Floor collision
    if (player.y + playerRadius >= height - 38 || player.y - playerRadius <= 0) {
      triggerGameOver();
      return;
    }
  } else if (gameState === 'START' || gameState === 'HOVER') {
    player.y = height * 0.45 + Math.sin(frameCount * 0.07) * 9;
    player.rotation = Math.sin(frameCount * 0.05) * 0.08;
  }
}

// 1. WHEN DEATH (NO POPUPS / NO REDIRECTS)
function triggerGameOver() {
  gameState = 'GAMEOVER';
  triggerScreenShake(16);
  createBottleShatter(player.x, player.y, 40);

  // Red screen flash
  redFlash.style.opacity = '0.7';
  setTimeout(() => redFlash.style.opacity = '0', 200);

  // PLAY AUDIO 1 (DEATH AUDIO)
  audioManager.playDeathAudio();

  // Populate modal
  finalScoreEl.innerText = score;
  bestScoreEl.innerText = bestScore;

  // Show modal
  setTimeout(() => {
    gameoverOverlay.style.display = 'flex';
  }, 250);
}

// 3. AFTER ENTERING THE GAME
function enterGame() {
  startOverlay.style.display = 'none';
  gameState = 'PLAYING';
  score = 0;
  updateScoreUI();
  obstacles = [];
  particles = [];
  player.reset();

  // Play Audio 3 (Intro Line)
  audioManager.playIntroAudio();
}

// PLAY AGAIN
function playAgain() {
  gameoverOverlay.style.display = 'none';
  gameState = 'PLAYING';
  score = 0;
  updateScoreUI();
  obstacles = [];
  particles = [];
  player.reset();

  // Play Audio 2 (Gameplay Music)
  audioManager.playGameplayAudio();
}

function render() {
  ctx.clearRect(0, 0, width, height);
  drawBackground();
  drawObstacles();
  drawParticles();
  drawPlayer();
}

function gameLoop() {
  update();
  render();
  requestAnimationFrame(gameLoop);
}

// --- EVENT LISTENERS ---
function handleUserAction(e) {
  if (e) {
    if (e.target.closest('.icon-btn') || 
        e.target.closest('.enter-game-btn') || 
        e.target.closest('.play-again-btn') ||
        e.target.closest('.side-ad-panel')) {
      return;
    }
  }

  if (gameState === 'START') {
    enterGame();
  } else if (gameState === 'PLAYING') {
    player.flap();

    if (!audioManager.audioGameplay.paused) {
      // already playing
    } else if (audioManager.audioIntro.paused || audioManager.audioIntro.currentTime > 2.5) {
      audioManager.playGameplayAudio();
    }
  }
}

window.addEventListener('keydown', (e) => {
  if (e.code === 'Space' || e.code === 'ArrowUp') {
    e.preventDefault();
    handleUserAction();
  }
});

gameContainer.addEventListener('pointerdown', handleUserAction);

enterGameBtn.addEventListener('click', (e) => {
  e.stopPropagation();
  enterGame();
});

playAgainBtn.addEventListener('click', (e) => {
  e.stopPropagation();
  playAgain();
});

// Sound Toggle Button
soundBtn.addEventListener('click', (e) => {
  e.stopPropagation();
  const enabled = audioManager.toggleMute();
  soundBtn.innerText = enabled ? '🔊' : '🔇';
});

// Avatar Skin Toggle (Classic vs Shades)
skinBtn.addEventListener('click', (e) => {
  e.stopPropagation();
  currentSkin = (currentSkin === 'CLASSIC') ? 'SHADES' : 'CLASSIC';
  skinBtn.innerText = (currentSkin === 'CLASSIC') ? '🕶️' : '🦁';
  showToast(currentSkin === 'CLASSIC' ? 'CLASSIC AVATAR' : 'SWAG SHADES!');
});

// Initialize
loadImages(() => {
  startBadgeImg.src = ASSETS.player_avatar;
  modalCardImg.src = ASSETS.modal_card;
  gameLoop();
});

// Register Monetag Service Worker for verification and Multitag
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').catch(function() {});
  });
}
</script>
<!-- Monetag In-Page Push / Banner Ads (Zone: 12162167) -->
<script>(function(s){s.dataset.zone='12162167',s.src='https://nap5k.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>
</body>
</html>
'''

# 1. Update balgame/index.html & Flying_Balayya_Game.html
with open(r'C:\Users\VINAY\Downloads\balgame\index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)
with open(r'C:\Users\VINAY\Downloads\balgame\Flying_Balayya_Game.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

# 2. Update Downloads/Flying_Balayya_Game.html
with open(r'C:\Users\VINAY\Downloads\Flying_Balayya_Game.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

# 3. Update Create arcade shooter game_files
with open(r'C:\Users\VINAY\Downloads\Create arcade shooter game_files\index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)
with open(r'C:\Users\VINAY\Downloads\Create arcade shooter game_files\runner.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print('Updated with Disclaimer banner and side ads successfully!')
