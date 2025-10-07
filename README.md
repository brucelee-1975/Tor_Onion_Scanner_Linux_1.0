# 🧅 Tor Fresh Onion Scanner Linux 1.0

[![Platform](https://img.shields.io/badge/Platform-Linux-yellow.svg)](https://www.linux.org/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)]()
[![Stars](https://img.shields.io/github/stars/yourusername/tor-scanner?style=social)]()

> **Professional darknet monitoring tool for Linux systems**  
> Continuously discovers fresh .onion addresses from clearnet sources.  
> **No Tor installation required!**

## 🎯 Overview

Tor Fresh Onion Scanner is a powerful Python-based tool that monitors public clearnet sources to discover new .onion addresses in real-time. Designed for security researchers, penetration testers, and cybersecurity enthusiasts working on Linux systems.

### ✨ Key Features

- 🔍 **24/7 Continuous Monitoring** - Never stops finding new onions
- 🐧 **Universal Linux Support** - Works on all major distributions
- 🎨 **Beautiful Terminal UI** - Colorful output with real-time updates
- 💾 **Smart Organization** - Auto-categorized file structure
- 📊 **Detailed Analytics** - Daily reports and comprehensive statistics
- 🚫 **No Tor Required** - Pure clearnet operation
- ⚡ **Multi-threaded** - Fast and efficient parallel scanning
- 🗄️ **SQLite Database** - Complete history with SQL query support
- 🔧 **Systemd Integration** - Run as system service with auto-start
- 🖥️ **Desktop Integration** - Application menu entry
- 📡 **Multiple Sources** - Aggregates from 4+ clearnet sources
- 🔄 **Auto-deduplication** - Smart filtering of duplicate entries

## 📋 Supported Distributions

<table>
<tr>
<td>

**Debian-based**
- Ubuntu (18.04+)
- Debian (9+)
- Kali Linux
- Linux Mint
- Pop!_OS
- Elementary OS
- Raspberry Pi OS

</td>
<td>

**Red Hat-based**
- Fedora (30+)
- CentOS (7+)
- RHEL (7+)
- Rocky Linux
- AlmaLinux

</td>
<td>

**Others**
- Arch Linux
- Manjaro
- EndeavourOS
- openSUSE
- Gentoo
- Alpine Linux

</td>
</tr>
</table>

## 🚀 Installation

### Quick Install (One-Line)

```bash
curl -sSL https://raw.githubusercontent.com/yourusername/tor-scanner/main/install_linux.sh | bash
```

### Standard Installation

```bash
# 1. Download installer
wget https://raw.githubusercontent.com/yourusername/tor-scanner/main/install_linux.sh

# 2. Make executable
chmod +x install_linux.sh

# 3. Run installer
./install_linux.sh
```

The installer automatically:
- ✅ Detects your Linux distribution
- ✅ Installs all required dependencies
- ✅ Creates scanner directory structure
- ✅ Sets up systemd service
- ✅ Configures desktop entry
- ✅ Initializes database

### Manual Installation

<details>
<summary>Click to expand manual installation steps</summary>

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-requests python3-bs4 sqlite3
pip3 install --user colorama lxml
```

#### Fedora
```bash
sudo dnf install -y python3 python3-pip python3-requests python3-beautifulsoup4 sqlite
pip3 install --user colorama lxml
```

#### Arch Linux
```bash
sudo pacman -S --noconfirm python python-pip python-requests python-beautifulsoup4 sqlite
pip install --user colorama lxml
```

#### Then clone and run
```bash
git clone https://github.com/yourusername/tor-scanner
cd tor-scanner
python3 tor_scanner.py
```

</details>

## 💻 Usage

### Basic Usage

```bash
cd ~/tor_scanner
./run.sh
```

### Background Mode (24/7)

```bash
cd ~/tor_scanner

# Start in background
./start_background.sh

# View live logs
tail -f scanner.log

# Stop scanner
./stop.sh
```

### System Service (Auto-start on Boot)

```bash
# Install service
sudo cp ~/tor_scanner/tor-scanner.service /etc/systemd/system/
sudo systemctl daemon-reload

# Enable auto-start
sudo systemctl enable tor-scanner

# Start service
sudo systemctl start tor-scanner

# Check status
sudo systemctl status tor-scanner

# View logs
sudo journalctl -u tor-scanner -f

# Stop service
sudo systemctl stop tor-scanner

# Disable auto-start
sudo systemctl disable tor-scanner
```

### Desktop Application

Add to your application menu:

```bash
cp ~/tor_scanner/tor-scanner.desktop ~/.local/share/applications/
update-desktop-database ~/.local/share/applications/
```

Now launch from your application menu! 🚀

## 📂 Directory Structure

```
~/tor_scanner/
│
├── tor_scanner.py              # Main scanner script
├── run.sh                      # Quick launcher
├── start_background.sh         # Background runner
├── stop.sh                     # Stop background process
├── tor-scanner.service         # Systemd service file
├── tor-scanner.desktop         # Desktop entry
├── onion_scanner.db            # SQLite database
├── scanner.pid                 # Process ID (when running)
├── scanner.log                 # Log file (background mode)
│
└── onion_results/              # ⭐ All results stored here
    │
    ├── MASTER_LIST.txt         # Complete list of all onions
    │
    ├── all_onions/             # All discoveries
    │   ├── all_2025-01-06.txt
    │   ├── all_2025-01-07.txt
    │   └── ...
    │
    ├── verified/               # Verified onions only
    │   └── verified_2025-01-06.txt
    │
    ├── marketplaces/           # Marketplace sites
    │   └── marketplaces_2025-01-06.txt
    │
    ├── forums/                 # Forum sites
    │   └── forums_2025-01-06.txt
    │
    ├── services/               # Service sites
    │   └── services_2025-01-06.txt
    │
    └── daily_logs/             # Statistics reports
        └── stats_2025-01-06.txt
```

## 📊 Output Format

### MASTER_LIST.txt

Complete, deduplicated list updated in real-time:

```
MASTER ONION LIST
Updated: 2025-01-06 15:30:45
Total: 1,234
================================================================================

3g2upl4pq6kufc4m.onion
abcdefghijklmnop.onion
example123456789.onion
...
```

### Daily Discovery Files

Detailed entries with metadata:

```
================================================================================
[2025-01-06 14:32:10] NEW ONION DISCOVERED
================================================================================
Address: example123abc456def.onion
Source: Dark.fail
Category: verified
Title: Hidden Wiki - Tor Links
Description: Directory of verified onion sites
Status: ✓ VERIFIED
```

### Statistics Reports

Daily analytics and metrics:

```
╔════════════════════════════════════════════════════════╗
║            DAILY STATISTICS REPORT                     ║
╚════════════════════════════════════════════════════════╝

Generated: 2025-01-06 23:59:59

SCAN STATISTICS:
  • Total Onions Found: 1,234
  • New This Session: 45
  • Verified Sites: 89
  • Marketplaces: 23
  • Forums: 67
  • Services: 34

SOURCES SCANNED:
  • Ahmia: 312 onions
  • Dark.fail: 145 onions
  • OnionLand: 287 onions
  • Tor.taxi: 198 onions

UPTIME:
  • Scanner uptime: 8:32:15
  • Cycles completed: 142
  • Average cycle time: 3.6 minutes
```

## 🔍 Data Sources

The scanner collects .onion addresses from these **public clearnet** sources:

| Source | Type | Description |
|--------|------|-------------|
| **Ahmia.fi** | Search Engine | Tor search engine with public listings |
| **Dark.fail** | Directory | Verified onion directory |
| **OnionLand** | Search Engine | Fresh onion discoveries |
| **Tor.taxi** | Directory | Curated onion directory |

**Important:** The scanner does NOT connect to actual .onion sites. It only collects publicly listed addresses from clearnet sources.

## 🛠️ Advanced Usage

### Database Queries

The scanner uses SQLite for persistent storage. Query examples:

```bash
# Access database
sqlite3 ~/tor_scanner/onion_scanner.db

# View all onions
SELECT * FROM onions;

# Count total onions
SELECT COUNT(*) FROM onions;

# Show only verified sites
SELECT address, title FROM onions WHERE verified=1;

# Recent discoveries (last 7 days)
SELECT address, first FROM onions 
WHERE first >= date('now', '-7 days') 
ORDER BY first DESC;

# Marketplaces only
SELECT address, title FROM onions 
WHERE category='marketplace';

# Search by keyword
SELECT address, title FROM onions 
WHERE title LIKE '%wiki%';

# Statistics by category
SELECT category, COUNT(*) as count 
FROM onions 
GROUP BY category 
ORDER BY count DESC;

# Export to CSV
.mode csv
.output onions.csv
SELECT * FROM onions;
.quit
```

### Filtering and Search

```bash
# Search in all files
grep -r "marketplace" ~/tor_scanner/onion_results/

# Count onions by category
find ~/tor_scanner/onion_results/ -name "*.txt" -exec wc -l {} +

# Extract only .onion addresses
grep -oP '[a-z2-7]{16,56}\.onion' ~/tor_scanner/onion_results/MASTER_LIST.txt

# Find today's discoveries
cat ~/tor_scanner/onion_results/all_onions/all_$(date +%Y-%m-%d).txt

# Count unique onions
sort ~/tor_scanner/onion_results/MASTER_LIST.txt | uniq | wc -l
```

### Automation with Cron

```bash
# Edit crontab
crontab -e

# Run scanner every 6 hours
0 */6 * * * cd ~/tor_scanner && ./start_background.sh

# Daily backup at 3 AM
0 3 * * * tar -czf ~/backups/tor_scanner_$(date +\%Y\%m\%d).tar.gz ~/tor_scanner/onion_results/

# Weekly cleanup of old logs
0 0 * * 0 find ~/tor_scanner/onion_results/ -name "*.txt" -mtime +30 -delete
```

### Export Options

```bash
# Export to JSON
sqlite3 ~/tor_scanner/onion_scanner.db << EOF
.mode json
.output onions.json
SELECT * FROM onions;
EOF

# Export to CSV
sqlite3 ~/tor_scanner/onion_scanner.db << EOF
.mode csv
.headers on
.output onions.csv
SELECT address, category, verified, title FROM onions;
EOF

# Export verified only
sqlite3 ~/tor_scanner/onion_scanner.db << EOF
.mode list
.output verified_onions.txt
SELECT address FROM onions WHERE verified=1;
EOF
```

## ⚙️ Configuration

### Scan Interval

Edit `~/tor_scanner/tor_scanner.py` (around line 380):

```python
wait = 180  # Default: 3 minutes

# Faster scanning (more CPU, network usage):
wait = 60   # 1 minute
wait = 120  # 2 minutes

# Slower scanning (less CPU, network usage):
wait = 300  # 5 minutes
wait = 600  # 10 minutes
```

### Thread Count

Edit `~/tor_scanner/tor_scanner.py` (around line 150):

```python
max_workers = 5  # Default

# Faster (more CPU):
max_workers = 10

# Slower (less CPU):
max_workers = 3
```

### Timeout Settings

```python
timeout = 10  # Default: 10 seconds

# Slower connections:
timeout = 15

# Faster connections:
timeout = 5
```

### Enable/Disable Sources

Comment out sources you don't want:

```python
sources = [
    self.ahmia,
    self.darkfail,
    self.onionland,
    # self.tortaxi,  # Disabled
]
```

## 🐛 Troubleshooting

### Python Not Found

```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

### Missing Dependencies

```bash
# Install all Python packages
pip3 install --user requests beautifulsoup4 colorama lxml

# Or use system packages (Ubuntu/Debian)
sudo apt install python3-requests python3-bs4

# Fedora
sudo dnf install python3-requests python3-beautifulsoup4

# Arch
sudo pacman -S python-requests python-beautifulsoup4
```

### Permission Errors

```bash
# Fix script permissions
chmod +x ~/tor_scanner/*.sh
chmod +x ~/tor_scanner/tor_scanner.py

# Fix directory permissions
chmod -R 755 ~/tor_scanner/
```

### Database Locked

```bash
# Remove journal file
rm ~/tor_scanner/onion_scanner.db-journal

# Or reset database
mv ~/tor_scanner/onion_scanner.db ~/tor_scanner/onion_scanner.db.backup
python3 ~/tor_scanner/tor_scanner.py
```

### Service Won't Start

```bash
# Check service status
sudo systemctl status tor-scanner

# View full error logs
sudo journalctl -xe -u tor-scanner

# Restart service
sudo systemctl restart tor-scanner

# Check permissions
ls -la ~/tor_scanner/

# Verify Python path in service file
which python3
# Update ExecStart in tor-scanner.service if needed
```

### Network Issues

```bash
# Test connectivity
ping -c 3 ahmia.fi
ping -c 3 dark.fail

# Check DNS
nslookup ahmia.fi

# Test with curl
curl -I https://ahmia.fi

# Disable firewall temporarily
sudo ufw disable  # Ubuntu
sudo systemctl stop firewalld  # Fedora
```

### High CPU Usage

```bash
# Reduce threads
# Edit tor_scanner.py: max_workers = 3

# Increase interval
# Edit tor_scanner.py: wait = 300

# Lower priority
nice -n 10 python3 tor_scanner.py

# Limit CPU (requires cpulimit)
cpulimit -l 50 -p $(cat ~/tor_scanner/scanner.pid)
```

## 🔒 Security & Privacy

### ⚠️ Important Disclaimers

- This tool operates **entirely on clearnet** (regular internet)
- **No Tor connection** is made or required
- Only collects **publicly available** information
- Does **NOT access** actual .onion sites
- For **educational and research purposes only**
- Users are **responsible** for legal compliance

### Safe Browsing Practices

If you wish to visit discovered .onion sites:

1. **Download official Tor Browser**
   ```bash
   # Ubuntu/Debian
   sudo apt install torbrowser-launcher
   torbrowser-launcher
   
   # Or download from: https://www.torproject.org/
   ```

2. **Use a VPN** before connecting to Tor for additional privacy

3. **Security rules:**
   - ❌ Never share personal information
   - ❌ Never download files from untrusted sources
   - ❌ Never conduct financial transactions
   - ❌ Never disable security features
   - ✅ Keep Tor Browser updated
   - ✅ Use HTTPS when available
   - ✅ Verify .onion addresses carefully

### Data Privacy

```bash
# Clear logs
rm ~/tor_scanner/scanner.log

# Clear old data
find ~/tor_scanner/onion_results/ -type f -mtime +30 -delete

# Encrypt results (requires gpg)
tar -czf - ~/tor_scanner/onion_results/ | gpg -c > onion_backup.tar.gz.gpg

# Secure delete (requires secure-delete)
srm -r ~/tor_scanner/onion_results/
```

## 📈 Monitoring & Statistics

### Real-time Monitoring

```bash
# Follow live logs
tail -f ~/tor_scanner/scanner.log

# Watch process
watch -n 1 'ps aux | grep tor_scanner'

# Monitor network
nethogs
iftop

# Resource usage
htop -p $(cat ~/tor_scanner/scanner.pid)
```

### Statistics Commands

```bash
# Total onions discovered
wc -l ~/tor_scanner/onion_results/MASTER_LIST.txt

# Today's discoveries
wc -l ~/tor_scanner/onion_results/all_onions/all_$(date +%Y-%m-%d).txt

# Count by category
sqlite3 ~/tor_scanner/onion_scanner.db << EOF
SELECT category, COUNT(*) as count 
FROM onions 
GROUP BY category 
ORDER BY count DESC;
EOF

# Verified vs unverified
sqlite3 ~/tor_scanner/onion_scanner.db << EOF
SELECT 
    SUM(CASE WHEN verified=1 THEN 1 ELSE 0 END) as verified,
    SUM(CASE WHEN verified=0 THEN 1 ELSE 0 END) as unverified
FROM onions;
EOF

# Growth over time
sqlite3 ~/tor_scanner/onion_scanner.db << EOF
SELECT date(first) as date, COUNT(*) as new_onions
FROM onions
GROUP BY date(first)
ORDER BY date DESC
LIMIT 30;
EOF
```

## 🎯 Performance Optimization

### For Servers

```bash
# Increase file descriptors
ulimit -n 4096

# Run with lower priority
nice -n 10 python3 tor_scanner.py

# Use ionice (reduce I/O priority)
ionice -c 3 python3 tor_scanner.py

# Combine nice and ionice
nice -n 10 ionice -c 3 python3 tor_scanner.py
```

### For VPS/Cloud

```bash
# Run as system service
sudo systemctl enable tor-scanner
sudo systemctl start tor-scanner

# Monitor resource usage
sudo systemctl status tor-scanner
htop
iotop
```

### For Raspberry Pi

```bash
# Reduce threads
# Edit: max_workers = 2

# Increase interval
# Edit: wait = 600  # 10 minutes

# Use swap if needed
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile  # CONF_SWAPSIZE=1024
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

### For Low-Memory Systems

```python
# Edit tor_scanner.py

# Reduce workers
max_workers = 2

# Smaller cache
self.session.max_redirects = 3

# Quick timeouts
timeout = 5
```

## 🔄 Updates & Maintenance

### Update Scanner

```bash
cd ~/tor_scanner

# Pull latest changes
git pull origin main

# Update dependencies
pip3 install --upgrade requests beautifulsoup4 colorama lxml

# Restart if running
./stop.sh
./start_background.sh

# Or restart service
sudo systemctl restart tor-scanner
```

### Backup Data

```bash
# Create backup
tar -czf ~/tor_scanner_backup_$(date +%Y%m%d).tar.gz ~/tor_scanner/

# Backup only results
tar -czf ~/onion_results_$(date +%Y%m%d).tar.gz ~/tor_scanner/onion_results/

# Backup database only
cp ~/tor_scanner/onion_scanner.db ~/backups/onion_scanner_$(date +%Y%m%d).db

# Restore backup
tar -xzf tor_scanner_backup_20250106.tar.gz -C ~/
```

### Clean Old Data

```bash
# Remove logs older than 30 days
find ~/tor_scanner/onion_results/ -name "*.txt" -mtime +30 -delete

# Compress old logs
find ~/tor_scanner/onion_results/ -name "*.txt" -mtime +7 -exec gzip {} \;

# Clean package cache
# Ubuntu/Debian
sudo apt clean

# Fedora
sudo dnf clean all

# Arch
sudo pacman -Sc
```

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/tor-scanner
cd tor-scanner

# 3. Create feature branch
git checkout -b feature-name

# 4. Make changes and test
python3 tor_scanner.py

# 5. Commit changes
git add .
git commit -m "Add feature: description"

# 6. Push to your fork
git push origin feature-name

# 7. Create Pull Request on GitHub
```

### Development Setup

```bash
# Install development dependencies
pip3 install --user pytest black flake8 mypy

# Run tests
pytest

# Format code
black tor_scanner.py

# Lint code
flake8 tor_scanner.py

# Type checking
mypy tor_scanner.py
```

## 📜 License

**Educational Use Only**

This software is provided for educational and research purposes only. Users are responsible for complying with all applicable laws and regulations in their jurisdiction.

## ⚠️ Legal Notice

- This software does not facilitate illegal activities
- Only collects publicly available information from clearnet sources
- No warranty or guarantee is provided
- Use at your own risk
- Comply with all applicable laws
- Respect website terms of service
- Do not abuse or overload source websites

## 📞 Support

### Getting Help

1. **Read this README** thoroughly
2. Check [Troubleshooting](#-troubleshooting) section
3. Search [existing issues](https://github.com/yourusername/tor-scanner/issues)
4. Create [new issue](https://github.com/yourusername/tor-scanner/issues/new) with:
   - Linux distribution and version
   - Python version (`python3 --version`)
   - Complete error message
   - Steps to reproduce
   - Relevant logs

### Useful Debug Commands

```bash
uname -a
cat /etc/os-release
python3 --version
pip3 --version

which python3
which pip3
pip3 list | grep -E "requests|beautifulsoup4|colorama"

ps aux | grep tor_scanner
cat ~/tor_scanner/scanner.pid

tail -50 ~/tor_scanner/scanner.log
journalctl -u tor-scanner -n 50

curl -I https://ahmia.fi
curl -I https://dark.fail

sqlite3 ~/tor_scanner/onion_scanner.db "SELECT COUNT(*) FROM onions;"
```

## 🎓 Resources

### Documentation
- [Tor Project Official](https://www.torproject.org/)
- [Python Documentation](https://docs.python.org/3/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Systemd Documentation](https://www.freedesktop.org/software/systemd/man/)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Learning
- [Darknet Research](https://www.darknetlive.com/)
- [Tor Hidden Services](https://community.torproject.org/onion-services/)
- [Web Scraping Ethics](https://en.wikipedia.org/wiki/Web_scraping)
- [Linux System Administration](https://www.tldp.org/)

### Tools
- [Tor Browser](https://www.torproject.org/download/)
- [Ahmia Search](https://ahmia.fi/)
- [Dark.fail Directory](https://dark.fail/)

## 🌟 Features Roadmap

- [ ] Web-based dashboard (Flask/FastAPI)
- [ ] REST API for integrations
- [ ] Docker containerization
- [ ] Kubernetes deployment
- [ ] Elasticsearch integration
- [ ] Grafana dashboards
- [ ] Real-time notifications (Email/Telegram)
- [ ] Machine learning classification
- [ ] Screenshot capture of clearnet references
- [ ] Historical trend analysis
- [ ] Network graph visualization
- [ ] Multi-language support
- [ ] Plugin system for custom sources
- [ ] Automated backup to cloud storage

## 💡 Tips & Tricks

```bash
systemctl is-active tor-scanner && echo "✅ Running" || echo "❌ Stopped"

wc -l ~/tor_scanner/onion_results/all_onions/all_$(date +%Y-%m-%d).txt

grep -oP '[a-z2-7]{56}\.onion' ~/tor_scanner/onion_results/MASTER_LIST.txt > addresses_only.txt

sort ~/tor_scanner/onion_results/MASTER_LIST.txt | uniq -d

diff <(sort old_master.txt) <(sort ~/tor_scanner/onion_results/MASTER_LIST.txt)

sqlite3 ~/tor_scanner/onion_scanner.db "SELECT address FROM onions WHERE verified=1" > verified.txt

cat <<EOF > daily_report_$(date +%Y-%m-%d).txt
Daily Onion Scanner Report
Generated: $(date)

Total onions: $(wc -l < ~/tor_scanner/onion_results/MASTER_LIST.txt)
New today: $(wc -l < ~/tor_scanner/onion_results/all_onions/all_$(date +%Y-%m-%d).txt)
Verified: $(sqlite3 ~/tor_scanner/onion_scanner.db "SELECT COUNT(*) FROM onions WHERE verified=1")
EOF

find ~/tor_scanner/onion_results/ -name "*.txt" -mtime +30 -exec gzip {} \;

gpg -c ~/tor_scanner/onion_results/MASTER_LIST.txt
```

## 📊 Performance Benchmarks

Typical performance on various systems:

| System | Cycle Time | Onions/Hour | CPU Usage | Memory |
|--------|-----------|-------------|-----------|---------|
| Desktop (8-core) | 2-3 min | ~150 | 5-10% | 80MB |
| Laptop (4-core) | 3-4 min | ~100 | 10-15% | 70MB |
| VPS (2-core) | 4-5 min | ~80 | 15-20% | 60MB |
| Raspberry Pi 4 | 5-7 min | ~50 | 20-30% | 50MB |

*Performance varies based on network speed and source availability*

## 🔗 Related Projects

- [OnionScan](https://github.com/s-rah/onionscan) - Onion service security scanner
- [TorBot](https://github.com/DedSecInside/TorBot) - Tor network intelligence tool
- [Ahmia](https://github.com/ahmia/ahmia-site) - Tor search engine
- [Fresh Onions](https://github.com/grugq/freshonions-torscraper) - Original onion scraper

## 🙏 Acknowledgments

- Tor Project for privacy technology
- Ahmia.fi for public onion indexing
- Dark.fail for verified directory
- Python community for excellent libraries
- Linux community for a great platform

---

<div align="center">

**Made with ❤️ for the Linux & Security Research community**

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/yourusername/tor-scanner)
[![Issues](https://img.shields.io/github/issues/yourusername/tor-scanner)](https://github.com/yourusername/tor-scanner/issues)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)]()

**⭐ Star this project if you find it useful!**

[Report Bug](https://github.com/yourusername/tor-scanner/issues) · [Request Feature](https://github.com/yourusername/tor-scanner/issues) · [Documentation](https://github.com/yourusername/tor-scanner/wiki)

</div>