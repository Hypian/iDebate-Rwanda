import os
import re

# We will create a standardized script that updates the 7 HTML files:
# 1. index.html
# 2. about.html
# 3. debate-league.html
# 4. teachers-debate-institute.html
# 5. international-program.html
# 6. student-training.html
# 7. contact.html

def generate_header(active_nav, current_page):
    is_home = active_nav == 'home'
    is_about = active_nav == 'about'
    is_programs = active_nav == 'programs'
    is_contact = active_nav == 'contact'

    home_cls = "text-primary dark:text-terracotta-sun border-b-2 border-primary dark:border-terracotta-sun font-semibold pb-1" if is_home else "text-on-surface-variant dark:text-paper-surface font-medium hover:text-primary dark:hover:text-terracotta-sun transition-colors duration-150 py-1"
    about_cls = "text-primary dark:text-terracotta-sun border-b-2 border-primary dark:border-terracotta-sun font-semibold pb-1" if is_about else "text-on-surface-variant dark:text-paper-surface font-medium hover:text-primary dark:hover:text-terracotta-sun transition-colors duration-150 py-1"
    prog_cls = "text-primary dark:text-terracotta-sun border-b-2 border-primary dark:border-terracotta-sun font-semibold pb-1" if is_programs else "text-on-surface-variant dark:text-paper-surface font-medium hover:text-primary dark:hover:text-terracotta-sun transition-colors duration-150 py-1"
    contact_cls = "text-primary dark:text-terracotta-sun border-b-2 border-primary dark:border-terracotta-sun font-semibold pb-1" if is_contact else "text-on-surface-variant dark:text-paper-surface font-medium hover:text-primary dark:hover:text-terracotta-sun transition-colors duration-150 py-1"

    return f'''<!-- 1. TOP DISPATCH BAR -->
<aside aria-label="Civic Dispatch Announcement" class="w-full bg-forest-deep text-paper-canvas border-b border-border-hairline/20 px-6 lg:px-16 py-2.5 select-none">
  <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2.5 text-label-caps font-label-caps">
    <div class="flex items-center gap-2.5">
      <span class="w-2 h-2 rounded-full bg-terracotta-sun animate-pulse shrink-0"></span>
      <span class="tracking-widest uppercase font-bold text-terracotta-sun hidden xs:inline">CIVIC DISPATCH:</span>
      <span class="tracking-wider text-paper-canvas">2025 NATIONAL DEBATE CALENDAR &amp; REGISTRATIONS ANNOUNCED</span>
    </div>
    <div class="flex items-center gap-4 lg:gap-6 text-paper-surface/90 text-[11px]">
      <a class="flex items-center gap-1.5 hover:text-terracotta-sun transition-colors" href="tel:+250790002626">
        <span class="material-symbols-outlined text-[15px] text-terracotta-sun">call</span>
        <span>+250 790 002 626</span>
      </a>
      <span class="text-border-hairline/40">|</span>
      <a class="flex items-center gap-1.5 hover:text-terracotta-sun transition-colors" href="mailto:info@debaterwanda.org">
        <span class="material-symbols-outlined text-[15px] text-terracotta-sun">mail</span>
        <span>info@debaterwanda.org</span>
      </a>
      <span class="text-border-hairline/40 hidden md:inline">|</span>
      <div class="hidden md:flex items-center gap-1.5 text-ochre-sand">
        <span class="material-symbols-outlined text-[15px]">public</span>
        <span>Kigali, Rwanda</span>
      </div>
    </div>
  </div>
</aside>

<!-- 2. UNIFIED EDITORIAL HEADER & NAVIGATION -->
<header class="w-full border-b border-border-hairline bg-paper-canvas dark:bg-forest-deep sticky top-0 z-50">
  <div class="max-w-7xl mx-auto px-6 lg:px-16 h-20 lg:h-24 flex items-center justify-between">
    <!-- Brand Identity Anchor -->
    <a class="flex flex-col group text-decoration-none" href="index.html">
      <span class="text-headline-md font-headline-md font-bold text-on-surface dark:text-paper-canvas tracking-tight leading-none group-hover:text-primary transition-colors">
        iDebate Rwanda
      </span>
      <span class="text-label-caps font-label-caps text-primary dark:text-terracotta-sun tracking-widest uppercase text-[10px] mt-1">
        Voice &amp; Leadership Initiative
      </span>
    </a>

    <!-- Desktop Navigation Cluster -->
    <nav class="hidden md:flex items-center gap-8 text-body-md font-body-md font-semibold" aria-label="Main Navigation">
      <a class="{home_cls}" href="index.html">Home</a>
      <a class="{about_cls}" href="about.html">About</a>

      <!-- Programs Dropdown Menu -->
      <div class="relative group py-2">
        <button type="button" class="{prog_cls} flex items-center gap-1 cursor-pointer focus:outline-none bg-transparent border-0 p-0">
          <span>Programs</span>
          <span class="material-symbols-outlined text-[18px] group-hover:rotate-180 transition-transform duration-200">expand_more</span>
        </button>
        <div class="absolute top-full left-0 w-64 pt-2 hidden group-hover:block transition-all duration-150 z-50">
          <div class="bg-paper-surface border border-border-hairline shadow-md p-2 space-y-1">
            <a class="block px-3 py-2 text-body-md font-body-md text-on-surface hover:bg-surface-container-low hover:text-primary transition-colors" href="student-training.html">
              Student Training
            </a>
            <a class="block px-3 py-2 text-body-md font-body-md text-on-surface hover:bg-surface-container-low hover:text-primary transition-colors" href="debate-league.html">
              Debate League
            </a>
            <a class="block px-3 py-2 text-body-md font-body-md text-on-surface hover:bg-surface-container-low hover:text-primary transition-colors" href="teachers-debate-institute.html">
              Teachers' Debate Institute
            </a>
            <a class="block px-3 py-2 text-body-md font-body-md text-on-surface hover:bg-surface-container-low hover:text-primary transition-colors" href="international-program.html">
              International Program (US Tour)
            </a>
            <a class="block px-3 py-2 text-body-md font-body-md text-on-surface hover:bg-surface-container-low hover:text-primary transition-colors" href="index.html#pillars">
              All Pillars Overview
            </a>
          </div>
        </div>
      </div>

      <a class="text-on-surface-variant dark:text-paper-surface font-medium hover:text-primary dark:hover:text-terracotta-sun transition-colors duration-150 py-1" href="about.html#alumni">Alumni</a>
      <a class="{contact_cls}" href="contact.html">Contact</a>
    </nav>

    <!-- Trailing Action: Quick Contact & Make Donation CTA -->
    <div class="flex items-center gap-3 lg:gap-4">
      <div class="hidden xl:flex items-center gap-2 pr-3 border-r border-border-hairline text-on-surface-variant">
        <a class="p-1.5 hover:text-primary transition-colors" href="tel:+250790002626" title="Telephone Secretariat">
          <span class="material-symbols-outlined text-[20px]">call</span>
        </a>
        <a class="p-1.5 hover:text-primary transition-colors" href="mailto:info@debaterwanda.org" title="Email Inquiries">
          <span class="material-symbols-outlined text-[20px]">mail</span>
        </a>
      </div>
      <a class="bg-primary hover:bg-terracotta-sun text-white font-label-caps text-label-caps px-5 lg:px-6 py-3 border border-primary transition-all duration-150 active:scale-[0.99] flex items-center gap-2" href="https://www.every.org/idebate-rwanda-rw" rel="noopener noreferrer" target="_blank">
        <span>Make Donation</span>
        <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
      </a>
      
      <!-- Mobile Menu Hamburger Button -->
      <button type="button" id="mobile-menu-toggle" aria-label="Toggle Mobile Menu" class="md:hidden p-2 text-on-surface hover:text-primary focus:outline-none bg-transparent border-0">
        <span class="material-symbols-outlined text-[28px]">menu</span>
      </button>
    </div>
  </div>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-nav-drawer" class="hidden md:hidden border-t border-border-hairline bg-paper-surface px-6 py-5 space-y-4">
    <div class="flex flex-col space-y-3 font-semibold text-body-md">
      <a class="text-on-surface hover:text-primary py-1" href="index.html">Home</a>
      <a class="text-on-surface hover:text-primary py-1" href="about.html">About Us</a>
      <div class="border-l-2 border-primary pl-3 py-1 space-y-2">
        <span class="font-label-caps text-xs text-primary uppercase font-bold tracking-wider block">Programs</span>
        <a class="block text-sm text-on-surface-variant hover:text-primary py-0.5" href="student-training.html">Student Training</a>
        <a class="block text-sm text-on-surface-variant hover:text-primary py-0.5" href="debate-league.html">Debate League</a>
        <a class="block text-sm text-on-surface-variant hover:text-primary py-0.5" href="teachers-debate-institute.html">Teachers' Debate Institute</a>
        <a class="block text-sm text-on-surface-variant hover:text-primary py-0.5" href="international-program.html">International Program (US Tour)</a>
      </div>
      <a class="text-on-surface hover:text-primary py-1" href="about.html#alumni">Alumni Impact</a>
      <a class="text-on-surface hover:text-primary py-1" href="contact.html">Contact</a>
    </div>
  </div>
</header>
'''

def generate_footer():
    return '''<!-- MONUMENTAL EDITORIAL FOOTER -->
<footer class="w-full border-t border-border-hairline/20 bg-forest-deep text-paper-canvas px-6 lg:px-16 py-16">
  <div class="max-w-7xl mx-auto">
    <!-- Top 4 Columns Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-10 lg:gap-12 pb-14 border-b border-border-hairline/20">
      <!-- Column 1: Institutional Statement (4 cols) -->
      <div class="lg:col-span-4 space-y-4">
        <a class="flex flex-col group" href="index.html">
          <span class="text-headline-md font-headline-md font-bold text-paper-canvas tracking-tight">
            iDebate Rwanda
          </span>
          <span class="text-label-caps font-label-caps text-terracotta-sun uppercase tracking-widest text-[10px] mt-0.5">
            Voice &amp; Leadership Initiative
          </span>
        </a>
        <p class="font-body-md text-body-md text-paper-surface/80 leading-relaxed max-w-sm">
          A premier non-governmental organization cultivating critical thinking, civil debate, and ethical public discourse among Rwandan youth and educators since 2012.
        </p>
        <div class="pt-2 flex items-center gap-3">
          <a class="w-9 h-9 border border-border-hairline/40 flex items-center justify-center text-paper-surface hover:text-white hover:border-terracotta-sun hover:bg-terracotta-sun transition-all duration-150" href="tel:+250790002626" title="Call Us">
            <span class="material-symbols-outlined text-[18px]">call</span>
          </a>
          <a class="w-9 h-9 border border-border-hairline/40 flex items-center justify-center text-paper-surface hover:text-white hover:border-terracotta-sun hover:bg-terracotta-sun transition-all duration-150" href="mailto:info@debaterwanda.org" title="Email Secretariat">
            <span class="material-symbols-outlined text-[18px]">mail</span>
          </a>
          <a class="w-9 h-9 border border-border-hairline/40 flex items-center justify-center text-paper-surface hover:text-white hover:border-terracotta-sun hover:bg-terracotta-sun transition-all duration-150" href="contact.html" title="Kigali Office Landmark">
            <span class="material-symbols-outlined text-[18px]">public</span>
          </a>
        </div>
      </div>

      <!-- Column 2: Navigation & Programs (3 cols) -->
      <div class="lg:col-span-3 space-y-4">
        <span class="text-label-caps font-label-caps text-terracotta-sun uppercase tracking-widest block">
          Pillars &amp; Academies
        </span>
        <ul class="space-y-2.5 font-body-md text-body-md text-paper-surface/80">
          <li><a class="hover:text-paper-canvas hover:translate-x-1 transition-all duration-150 inline-block" href="debate-league.html">Debate League</a></li>
          <li><a class="hover:text-paper-canvas hover:translate-x-1 transition-all duration-150 inline-block" href="teachers-debate-institute.html">Teachers' Debate Institute</a></li>
          <li><a class="hover:text-paper-canvas hover:translate-x-1 transition-all duration-150 inline-block" href="student-training.html">Student Training</a></li>
          <li><a class="hover:text-paper-canvas hover:translate-x-1 transition-all duration-150 inline-block" href="international-program.html">International Program (US Tour)</a></li>
          <li><a class="hover:text-paper-canvas hover:translate-x-1 transition-all duration-150 inline-block" href="about.html#alumni">Alumni Stories</a></li>
        </ul>
      </div>

      <!-- Column 3: Headquarters & Contact (2 cols) -->
      <div class="lg:col-span-2 space-y-4">
        <span class="text-label-caps font-label-caps text-terracotta-sun uppercase tracking-widest block">
          Headquarters
        </span>
        <div class="font-body-md text-body-md text-paper-surface/80 space-y-3">
          <p class="leading-relaxed">
            Ikaze House, Floor 3<br/>
            24R6+F55 KG 11 Ave<br/>
            Gasabo Sector, Kigali
          </p>
          <p class="pt-1">
            <strong class="text-paper-canvas block text-xs tracking-wider">DIRECT TELEPHONE</strong>
            <a class="hover:text-terracotta-sun transition-colors" href="tel:+250790002626">+250 790 002 626</a>
          </p>
          <p>
            <strong class="text-paper-canvas block text-xs tracking-wider">OFFICIAL INQUIRIES</strong>
            <a class="hover:text-terracotta-sun transition-colors" href="mailto:info@debaterwanda.org">info@debaterwanda.org</a>
          </p>
        </div>
      </div>

      <!-- Column 4: Newsletter Dispatch (3 cols) -->
      <div class="lg:col-span-3 space-y-4">
        <span class="text-label-caps font-label-caps text-terracotta-sun uppercase tracking-widest block">
          The Civic Dispatch
        </span>
        <p class="font-body-md text-body-md text-paper-surface/80 leading-relaxed">
          Receive our educational monographs, debate motion dossiers, and civic leadership reports directly to your inbox.
        </p>
        <form class="space-y-2.5" onsubmit="event.preventDefault(); alert('Thank you for subscribing to the iDebate Civic Dispatch.');">
          <div class="relative">
            <input class="w-full bg-forest-deep border border-border-hairline/40 text-paper-canvas placeholder-paper-surface/40 px-3.5 py-2.5 text-body-md font-body-md focus:border-terracotta-sun focus:ring-0 focus:outline-none rounded-none" placeholder="Enter your academic email" required="" type="email"/>
          </div>
          <button class="w-full bg-terracotta-sun hover:bg-primary text-white font-label-caps text-label-caps py-3 transition-colors duration-150 uppercase tracking-wider text-center cursor-pointer" type="submit">
            Subscribe to Journal
          </button>
        </form>
      </div>
    </div>

    <!-- Bottom Attribution & Legal -->
    <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-body-md font-body-md text-paper-surface/60">
      <p class="text-center md:text-left text-xs sm:text-sm">
        &copy; 2025 iDebate Rwanda. Cultivating critical debate, ethical leadership, and civil discourse. All rights reserved.
      </p>
      <div class="flex items-center gap-6 text-xs uppercase tracking-wider">
        <a class="hover:text-paper-canvas transition-colors" href="contact.html">Contact Us</a>
        <span>•</span>
        <a class="hover:text-paper-canvas transition-colors" href="about.html">About Us</a>
        <span>•</span>
        <a class="hover:text-paper-canvas transition-colors" href="https://www.every.org/idebate-rwanda-rw" target="_blank" rel="noopener noreferrer">Make Donation</a>
      </div>
    </div>
  </div>
</footer>

<script>
  // Shared Mobile Navigation Drawer Toggle Script
  document.addEventListener('DOMContentLoaded', function() {
    var toggleBtn = document.getElementById('mobile-menu-toggle');
    var drawer = document.getElementById('mobile-nav-drawer');
    if (toggleBtn && drawer) {
      toggleBtn.addEventListener('click', function() {
        drawer.classList.toggle('hidden');
      });
    }
  });
</script>
'''

print("Standardizer functions compiled.")
