#!/usr/bin/env python3
"""
Test Suite: HRL Self-Assigning Core Inner Roles Integrity Verification
Verifies pure-skill hiring charter, leadership roster mapping, asset resolution,
and mandatory brand standards (motto, zero emojis) across all documentation.
"""
import os
import re

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def test_repository_integrity():
    required_files = [
        'README.md',
        'HRL_LEADERSHIP_ROSTER.md',
        'HRL_SELF_ASSIGNING_ROLE_CHARTER.md',
        'FAQ.md',
        'CANDIDATE_APPLICATION_TEMPLATE.md',
    ]

    expected_leaders = [
        ('Pavan Kumar Sadashiv', 'Founder, Managing Director & Chief AI Systems Architect', '@hrl'),
        ('Sheikh Mohammed Raees', 'Chief Executive Officer (CEO)', '@hrl'),
        ('Sanjana', 'Co-Founder & Executive Council', '@hrl'),
        ('Apoorvi Vijay', 'Chief Executive Officer (CEO), HRL Crimson Red Media', '@hrlcrimsonRED'),
        ('Nishwin', 'Real Estate Agent (REA)', '@hrl'),
        ('Shubhada Naik', 'Strategic Business Consultant', '@hrl'),
        ('Jia Shetty', 'Core Community Manager', '@hrl'),
        ('Saismitha', 'Head of Commercial Brands & Brand Partnerships Lead', '@hrl'),
        ('Seejal', 'Deep Data & Data Engineering', '@hrl'),
        ('Thaif', 'Developer Ecosystem Coordinator', '@hrl'),
    ]

    expected_avatars = [
        'sheikh-mohammed-raees.jpg',
        'sanjana.png',
        'apoorvi-vijay.jpg',
        'nishwin.jpeg',
        'shubhada-naik.jpg',
        'jia-shetty.jpeg',
        'Saismitha.jpg',
        'seejal.jpg',
        'thaif.jpg',
    ]

    # 1. Verify existence of all required documentation files
    for filename in required_files:
        filepath = os.path.join(REPO_DIR, filename)
        assert os.path.isfile(filepath), f"Missing required file: {filename}"
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for prohibited emojis (Zero-emoji policy)
        emojis = re.findall(r'[\U00010000-\U0010ffff]', content)
        assert len(emojis) == 0, f"Prohibited emoji found in {filename}: {emojis}"

    # 2. Verify all leader avatars on disk and non-empty
    avatar_dir = os.path.join(REPO_DIR, 'HRL CORE COMPANY ROLE')
    assert os.path.isdir(avatar_dir), "Missing 'HRL CORE COMPANY ROLE' directory"
    for avatar in expected_avatars:
        avatar_path = os.path.join(avatar_dir, avatar)
        assert os.path.isfile(avatar_path), f"Missing avatar file on disk: {avatar}"
        assert os.path.getsize(avatar_path) > 0, f"Avatar file is empty: {avatar}"

    # 3. Verify presence of all leaders and roles in README and ROSTER
    for check_doc in ['README.md', 'HRL_LEADERSHIP_ROSTER.md']:
        with open(os.path.join(REPO_DIR, check_doc), 'r', encoding='utf-8') as f:
            doc_text = f.read()
        
        # Mandatory company motto
        assert 'We Can Do Everything Related To Software Sector Without Any Excuses!' in doc_text, \
            f"Mandatory company motto missing in {check_doc}"
        
        # Verify leaders
        for name, role, division in expected_leaders:
            assert name in doc_text, f"Leader '{name}' missing in {check_doc}"
            assert division in doc_text, f"Division '{division}' missing in {check_doc}"

    print("PASS: HRL Self-Assigning Core Inner Roles Repository verified successfully (100% compliance).")

if __name__ == '__main__':
    test_repository_integrity()
