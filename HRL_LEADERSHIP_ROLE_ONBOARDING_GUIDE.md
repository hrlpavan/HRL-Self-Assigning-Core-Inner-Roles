# HRL International Private Limited™ — Leadership Architecture & Role Onboarding Protocol

**Document Status**: Official Corporate Standard & Future Role Ingestion Specification  
**Authority**: HRL International Private Limited™  
**Founder & Managing Director**: Pavan Kumar Sadashiv (`hrlpavan`)  
**Standard Identifier**: `HRL-SPEC-LEADERSHIP-ONBOARDING-2026-V1`  
**Effective Date**: October 2026  
**Target Repositories**: `hrl-international-website-`, `HRL-Company-Page-Announcement-Design`, and `HRL-Self-Assigning-Core-Inner-Roles`  
**Hiring & Role Discovery Portal**: [https://github.com/hrlpavan/HRL-Self-Assigning-Core-Inner-Roles](https://github.com/hrlpavan/HRL-Self-Assigning-Core-Inner-Roles)  

---

## 1. Overview & Purpose of This Architecture Update

This update establishes a standalone, dedicated **Corporate Leadership Directory (`/leadership`)** for HRL International Private Limited to showcase our executive council, founders, and division managers, loading all profile pictures dynamically from the **`HRL CORE COMPANY ROLE`** directory.

### Core Architecture Objectives
1. **Dedicated Executive Showcase**: Independent route (`/leadership` and `/leadership.html`) decoupling executive governance from the landing page.
2. **Tactile Identity Card Design Language**: Direct inheritance of the Universal Rate Card & Studio VFX standard (baby pink accent stripe, subtle rose gradient, tactile drop shadows, and typographic watermarks).
3. **High-Fidelity Specular Glass Avatar Lenses**: Optical mirror glare, diagonal lens horizon reflections, and continuous $360^\circ$ specular conic chrome rims.
4. **Instagram-Ready High-Definition PNG Card Export**: One-click client-side HD PNG rendering at 3x pixel ratio (~1140×1650 px at 300 DPI) optimized for immediate posting to Instagram feeds and stories.
5. **Symmetrical Placing Principle**: Balanced responsive grid (3 columns on desktop, 2 on tablet, 1 on mobile) with zero lone dangling cards.
6. **Zero Main Page Regression**: The main page (`index.html`) remains clean and regression-free, with surgical navigation links inserted into the navbar and footer.

---

## 2. Design Tokens & Visual Architecture

### A. Color Palette & Card Shell Tokens
| Token | Value | Visual Function |
| :--- | :--- | :--- |
| **Surface Background** | `linear-gradient(165deg, #ffffff 0%, #fff7f9 100%)` | Subtle tactile rose-white executive gradient. |
| **Accent Stripe (`@hrl`)** | `#e05375` (`border-left: 5px solid #e05375`) | Primary tactile boundary stripe on left edge. |
| **Accent Stripe (`@hrlcrimsonRED`)** | `#D1002D` (`border-left: 5px solid #D1002D`) | High-salience Crimson Red division boundary stripe. |
| **Card Border** | `1px solid rgba(255, 182, 193, 0.45)` | Subtle translucent rose containment boundary. |
| **Border Radius** | `20px` (`var(--radius-card)`) | Apple-caliber rounded geometry. |
| **Box Shadow** | `0 16px 36px rgba(255, 182, 193, 0.14), 0 2px 8px rgba(0, 0, 0, 0.02)` | Tactile soft elevation. |
| **Hover State** | `transform: translateY(-4px); border-left-color: #D1002D;` | Tactile elevation with enriched drop shadow. |

### B. High-Quality Specular Glass Avatar Lens & Mirror Reflection
Every leader profile avatar features a multi-layer specular glass lens engineered for 100% cross-browser reliability (Safari/WebKit & Blink compatible with zero masking artifacts):

1. **Native Conic Chrome Rim (`.avatar-wrapper`)**:
   * Continuous $360^\circ$ metallic silver/chrome transition with zero blank spots applied via native CSS conic gradient on the wrapper with 3px padding:
     ```css
     .avatar-wrapper {
       width: 146px;
       height: 146px;
       border-radius: 50%;
       padding: 3px;
       box-sizing: border-box;
       background: conic-gradient(
         from 225deg,
         #ffffff 0deg, #cbd5e1 35deg, #64748b 70deg, #334155 120deg,
         #0f172a 160deg, #1e293b 200deg, #475569 230deg, #94a3b8 270deg,
         #e2e8f0 310deg, #ffffff 340deg, #ffffff 360deg
       );
       box-shadow: 0 4px 14px rgba(0, 0, 0, 0.22), 0 1px 3px rgba(0, 0, 0, 0.12);
     }
     ```
   * Crimson variant (`.avatar-wrapper.crimson-rim`) for `@hrlcrimsonRED` transitioning from white to scarlet (`#D1002D`), deep garnet (`#881337`), and ruby highlights.
2. **Specular Glass Mirror Reflection & Lens Horizon (`::after`)**:
   * Overlaid optical glare at `inset: 3px; z-index: 2`:
     * **Upper $45^\circ$ Diagonal Lens Horizon Mirror Sheen**: `linear-gradient(135deg, rgba(255,255,255,0.38) 0%, rgba(255,255,255,0.15) 28%, rgba(255,255,255,0.02) 48%, transparent 52%, rgba(255,255,255,0.03) 75%, rgba(255,255,255,0.12) 100%)`
     * **Top Radial Studio Keylight Flare**: `radial-gradient(ellipse at 50% 0%, rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.12) 32%, transparent 65%)`
   * **Double-Lipped Beveled Glass Edge**:
     ```css
     box-shadow: 
       inset 0 1.5px 2px rgba(255, 255, 255, 0.90),
       inset 0 -1.5px 2px rgba(0, 0, 0, 0.35),
       inset 0 0 0 1px rgba(255, 255, 255, 0.20);
     ```

### C. Background Watermark Monogram
* Large translucent typography anchored at `right: -15px; bottom: -15px;` with:
  `font-size: 88px; font-weight: 900; color: rgba(224, 83, 117, 0.05); line-height: 1; pointer-events: none; user-select: none;`

### D. Instagram Story 9:16 HD Export & QR Verification Engine
* **Libraries**: `assets/js/html-to-image.min.js` and `assets/js/qrcode.min.js` (locally vendored, 100% offline).
* **Ratio & Resolution**: Exact **9:16 aspect ratio** rendered at **1080 × 1920 px** (via 540×960 wrapper scaled at 2x), with `imageSmoothingQuality = 'high'`, matching Instagram Story safe zones without stretching or blur.
* **Preloaded Base64 Image Pipeline**: All avatar images (`crossorigin="anonymous"`, `loading="eager"`) are converted to Base64 Data URLs prior to capture, eliminating canvas tainting or blank image failures.
* **Dynamic Export QR Code**: During export, `.card-actions-row` is swapped with `.card-export-qr-row`, generating a 56×56 px scannable QR code linking to `https://hrlpavan.github.io/hrl-international-website-/` alongside verification helper text.
* **Filename Standard**: `HRL_Leadership_[Sanitized_Name]_Story_9x16.png` (e.g. `HRL_Leadership_Sheikh_Mohammed_Raees_Story_9x16.png`).

---

## 3. Protocol for Adding a New Role in the Future

Whenever a new executive, founder, director, or operational manager joins HRL, follow this **5-Phase Onboarding Protocol**:

### Phase 1: Asset Intake
1. Obtain an executive headshot or professional portrait.
2. Crop/format the image to a **1:1 square ratio** (minimum `800 × 800 px`, ideal `1080 × 1080 px`).
3. Save the image into the **`HRL CORE COMPANY ROLE`** folder:
   * Filename convention: `firstname-lastname.jpg` (or `.png` / `.jpeg`)
   * Lowercase, hyphen-separated, zero spaces.
   * Example: `HRL CORE COMPANY ROLE/alex-rivera.jpg`

### Phase 2: Role Metadata Specification
Prepare the following metadata attributes:
* **Full Legal / Corporate Name**: e.g., `Alex Rivera`
* **Corporate Designation / Title**: e.g., `Chief Technology Officer (CTO)`
* **Division Tag**:
  * `@hrl`: Core sovereign software, AI research, cloud infrastructure, enterprise engineering.
  * `@hrlcrimsonRED`: Digital media broadcasting, Hollywood film promotions, creator acceleration, VFX.
* **Category Pill Tag**: e.g., `HRL Technology Directorate` or `HRL Creative Directorate`
* **Strategic Role Scope (2–3 lines)**: Executive summary of domain ownership and operational mandate.
* **Watermark Monogram (2–3 characters)**: e.g., `CTO`, `COO`, `DIR`, `VP`, `LEAD`.

### Phase 3: Symmetrical Grid Verification
Before publishing, ensure the total number of leaders maintains the **Symmetrical Placing Principle**:
* Multiples of **2** or **3** items are required.
* 6 cards = 2 rows of 3 (desktop) | 3 rows of 2 (tablet).
* If adding 1 new role (making 7), pair it with a second role (making 8: 2×4 or 4×2) or reorganize into 2 balanced sections (e.g. Executive Board: 3 members; Operational Directorate: 4 members in 2×2).

### Phase 4: Code Insertion (HTML Template)
Copy and paste the production template below into both `leadership.html` and `leadership/index.html`.

---

## 4. Production Card Code Template for New Roles

### Standard Role Card (`@hrl` Division)
```html
<article class="tactile-identity-card">
  <!-- 1. Background Watermark Monogram -->
  <div class="card-watermark">[MONOGRAM]</div>

  <div>
    <!-- 2. Eyebrow Category Pill -->
    <div class="card-eyebrow-pill">
      <span class="pill-dot"></span>
      <span class="pill-text">[CATEGORY BADGE, e.g. HRL Technology Directorate]</span>
    </div>

    <!-- 3. Specular Glass Avatar Lens with Mirror Glare -->
    <div class="avatar-hero-container">
      <div class="avatar-wrapper">
        <img 
          src="HRL%20CORE%20COMPANY%20ROLE/[filename.jpg]" 
          alt="[Full Name] — [Title]" 
          class="avatar-img"
          crossorigin="anonymous"
          loading="eager"
          onerror="this.onerror=null; this.src='assets/hrl-company-avatar.png';"
        />
      </div>
    </div>

    <!-- 4. Identity & Scope Block -->
    <div class="card-title-group">
      <h2 class="card-main-title">[Full Name]</h2>
      <div class="card-accent-subhead">[Official Title, e.g. Chief Technology Officer (CTO)]</div>
      <p class="card-body-desc">
        [Concise 2-line strategic scope describing operational mandate and enterprise domain].
      </p>
      <div class="division-tag-row">
        <span class="division-pill division-pill-hrl">
          <span class="pill-dot"></span>
          @hrl
        </span>
      </div>
    </div>
  </div>

  <!-- 5. Signature Tactile Metadata Footer with 9:16 PNG Export & QR -->
  <div class="card-tactile-footer">
    <div class="card-footer-name">[FULL NAME IN UPPERCASE] (HRL)</div>
    <div class="card-footer-meta">[Official Corporate Title] · HRL International Private Limited</div>
    <div class="card-actions-row">
      <button type="button" class="card-download-btn" onclick="downloadLeadershipCard(this, '[Full Name]')" title="Download Card as PNG (Instagram Story 9:16 HD)">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        <span>Download Card (PNG)</span>
      </button>
    </div>
    <div class="card-export-qr-row">
      <div class="qr-code-box"></div>
      <div class="qr-text-col">
        <div class="qr-helper-line1">Scan to verify &amp; connect</div>
        <div class="qr-helper-line2">hrlpavan.github.io/hrl-international-website-/</div>
      </div>
    </div>
  </div>
</article>
```

### Crimson Red Media Role Card (`@hrlcrimsonRED` Division)
```html
<article class="tactile-identity-card card-crimson">
  <!-- 1. Background Watermark Monogram -->
  <div class="card-watermark">[MONOGRAM]</div>

  <div>
    <!-- 2. Eyebrow Category Pill -->
    <div class="card-eyebrow-pill">
      <span class="pill-dot"></span>
      <span class="pill-text">[CATEGORY BADGE, e.g. HRL Crimson Red Media]</span>
    </div>

    <!-- 3. Specular Glass Avatar Lens (Crimson Conic Rim) -->
    <div class="avatar-hero-container">
      <div class="avatar-wrapper crimson-rim">
        <img 
          src="HRL%20CORE%20COMPANY%20ROLE/[filename.jpg]" 
          alt="[Full Name] — [Title]" 
          class="avatar-img"
          crossorigin="anonymous"
          loading="eager"
          onerror="this.onerror=null; this.src='assets/hrl-company-avatar.png';"
        />
      </div>
    </div>

    <!-- 4. Identity & Scope Block -->
    <div class="card-title-group">
      <h2 class="card-main-title">[Full Name]</h2>
      <div class="card-accent-subhead">[Official Title]</div>
      <p class="card-body-desc">
        [Concise 2-line strategic scope describing media engineering and broadcast production mandate].
      </p>
      <div class="division-tag-row">
        <span class="division-pill division-pill-crimson">
          <span class="pill-dot"></span>
          @hrlcrimsonRED
        </span>
      </div>
    </div>
  </div>

  <!-- 5. Signature Tactile Metadata Footer with 9:16 PNG Export & QR -->
  <div class="card-tactile-footer">
    <div class="card-footer-name">[FULL NAME IN UPPERCASE] (HRL)</div>
    <div class="card-footer-meta">[Official Corporate Title] · HRL Crimson Red Media</div>
    <div class="card-actions-row">
      <button type="button" class="card-download-btn" onclick="downloadLeadershipCard(this, '[Full Name]')" title="Download Card as PNG (Instagram Story 9:16 HD)">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        <span>Download Card (PNG)</span>
      </button>
    </div>
    <div class="card-export-qr-row">
      <div class="qr-code-box"></div>
      <div class="qr-text-col">
        <div class="qr-helper-line1">Scan to verify &amp; connect</div>
        <div class="qr-helper-line2">hrlpavan.github.io/hrl-international-website-/</div>
      </div>
    </div>
  </div>
</article>
```

> **Note for `leadership/index.html`**: Always prepend `../` to relative asset and page links (e.g. `../HRL%20CORE%20COMPANY%20ROLE/[filename.jpg]`, `../assets/...`, `../index.html`).

---

## 5. Automated Verification Checklist

After editing the files, run the automated test suite:

```bash
python3 test_leadership_page.py
```

The test runner will deterministically verify:
1. All referenced avatar images exist on disk and are non-empty.
2. Zero decorative emojis in HTML/CSS/JS (100% compliance).
3. Company motto presence and exact phrasing.
4. Correct division tags (`@hrl` or `@hrlcrimsonRED`).
5. Zero main page regressions (`git diff index.html` limited strictly to clean nav/footer links).

---

## 6. Current Verified Roster (Reference Baseline)

| Member | Title | Division | Image File | Watermark |
| :--- | :--- | :--- | :--- | :--- |
| **Sheikh Mohammed Raees** | Chief Executive Officer (CEO) | `@hrl` | `sheikh-mohammed-raees.jpg` | `CEO` |
| **Sanjana** | Co-Founder | `@hrl` | `sanjana.png` | `CO` |
| **Apoorvi Vijay** | Chief Executive Officer (CEO) | `@hrlcrimsonRED` | `apoorvi-vijay.jpg` | `CRM` |
| **Nishwin** | Real Estate Agent (REA) | `@hrl` | `nishwin.jpeg` | `REA` |
| **Shubhada Naik** | Business Consultant | `@hrl` | `shubhada-naik.jpg` | `BIZ` |
| **Jia Shetty** | Core Community Manager | `@hrl` | `jia-shetty.jpeg` | `CM` |
| **Saismitha** | Head of Commercial Brands & Brand Partnerships Lead | `@hrl` | `Saismitha.jpg` | `CB` |
| **Seejal** | Deep Data & Data Engineering | `@hrl` | `seejal.jpg` | `DATA` |
| **Thaif** | Developer Ecosystem Coordinator | `@hrl` | `thaif.jpg` | `DEV` |

---

## 7. Instagram Story 9:16 HD Card Export Standards & Bug Fix Specifications

When exporting leadership tactile cards for social media (Instagram Stories / 1080x1920 HD PNG), all role additions must adhere to the following 5 anti-glitch architectural guarantees:

1. **Avatar Pre-Decode & HTML5 Canvas Circular Clipping (Zero Corner Bleed / Zero Blank Canvas)**:
   - Square raster images must be pre-clipped directly on an HTML5 `<canvas>` using `ctx.arc(r, r, r, 0, Math.PI * 2); ctx.clip(); ctx.drawImage(...);` prior to generating the Base64 Data URL.
   - This physically replaces square bitmap corner data with 100% alpha transparency, eliminating WebKit SVG `foreignObject` square edge corner leakage and preventing blank white canvas renders.
   - An explicit pre-decode check (`if (!origImg.complete) await ...`) must precede canvas rasterization.

2. **Two-Layer Off-Screen Host Isolation (Zero Viewport Flash / Zero Visual Overlap)**:
   - The export tree must be hosted inside an outer container (`id="hrl-offscreen-host"`) fixed at `left: -9999px; overflow: hidden; pointer-events: none;`.
   - The inner export wrapper (`id="hrl-export-wrapper"`) maintains `position: relative; margin: 0; width: 540px; height: 960px;`.
   - This ensures the card renders at `(0, 0)` inside the SVG serialization canvas while physically sitting completely off-screen in the user's browser, preventing any visible flashing or overlapping card modals.

3. **Anti-Clipping Geometry & Shadow Breathing Room**:
   - The export wrapper must enforce `padding: 48px 40px` and the cloned card must restrict `max-width: 440px`.
   - This guarantees at least 50px of buffer around all 4 edges so high-blur tactile card shadows (`0 20px 48px`) are never sliced off into a vertical line.

4. **Anti-Truncation Flexbox Guard (QR Text Safety)**:
   - The QR text column (`.qr-text-col`) must enforce `flex: 1 1 auto; min-width: 0;`.
   - The verification lines must enforce `white-space: nowrap;` so URLs never wrap character-by-character into single-letter vertical slivers.

5. **Strict Cleanup**:
   - The `finally` block must unconditionally remove `#hrl-offscreen-host` from `document.body` to preserve DOM cleanliness.

---

## 8. The 3-Artifact LinkedIn Social & Profile Onboarding Standard

Whenever a batch of 3 new candidates (or an individual candidate) joins HRL International, the following 3 mandatory artifacts must be generated:

### Artifact 1: Main Company LinkedIn Post (3-Candidate Batch Announcement)
- **Format**: High-impact multi-image post attaching the 3 corresponding `1080x1920` 9:16 HD PNG cards in numeric sequence (`01_...`, `02_...`, `03_...`).
- **Required Elements**:
  - Hook featuring company entity: `HRL International Private Limited`.
  - Non-negotiable motto: *"We Can Do Everything Related To Software Sector Without Any Excuses!"*.
  - Founder recognition: `Pavan Kumar Sadashiv (Managing Director & Chief AI Systems Architect)`.
  - Summary of the 3 candidates with Name, Title, Domain Mandate, and Division Tag (`@hrl` or `@hrlcrimsonRED`).
  - Official directory link: `https://hrlpavan.github.io/hrl-international-website-/leadership.html`.
  - Corporate Inquiries: `hrlinternationalprivatelimited@gmail.com`.
  - Statutory HQ attribution: `Mangaluru, Karnataka, India`.
  - Strict zero-emoji policy.

### Artifact 2: Individual Candidate Spotlight Caption
- **Format**: Single-candidate deep-dive post paired with that candidate's standalone `1080x1920` 9:16 HD PNG card.
- **Required Elements**:
  - Candidate Name, Corporate Title, and Division.
  - Strategic role scope detailing core responsibilities and technical ownership.
  - Mandatory company motto and official verification URL.

### Artifact 3: Personal Candidate LinkedIn Experience Markdown (`.md`)
- **Format**: Stored in `HRL_LINKEDIN_EXPERIENCE_KIT.md` and provided privately to the candidate for immediate 1-click copy-paste.
- **Required Fields**:
  - **Title**: Exact Corporate Designation.
  - **Employment Type**: `Full-time`.
  - **Company Name**: `HRL International Private Limited` (or `HRL Crimson Red Media`).
  - **Location**: `Mangaluru, Karnataka, India`.
  - **Location Type**: `Hybrid` or `On-site`.
  - **Description**: 4–5 bullet points detailing core operational responsibilities, domain mandate, division tag, and official directory link.
  - **Top Skills**: 8–10 high-value technical/operational LinkedIn skills.
  - **Media Link**: `https://hrlpavan.github.io/hrl-international-website-/leadership.html`.

---
**Maintained by**: HRL International Private Limited Corporate Systems Directorate  
**Author & Inventor**: Pavan Kumar Sadashiv (`hrlpavan`)
