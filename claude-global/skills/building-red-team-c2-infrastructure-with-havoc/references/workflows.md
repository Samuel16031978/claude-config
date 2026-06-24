# Workflows: Havoc C2 Infrastructure Deployment

## Infrastructure Deployment Workflow

```
ÔöîÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÉ
Ôöé              HAVOC C2 DEPLOYMENT WORKFLOW                         Ôöé
Ôö£ÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöñ
Ôöé                                                                  Ôöé
Ôöé  1. DOMAIN & INFRASTRUCTURE PREPARATION (Week -4)                Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Register domain names (aged 30+ days)                    Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Submit domains for categorization (Bluecoat, Fortiguard) Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Provision VPS instances (Teamserver + Redirector)        Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Obtain SSL certificates (Let's Encrypt)                  Ôöé
Ôöé     ÔööÔöÇÔöÇ Configure DNS A records                                  Ôöé
Ôöé                                                                  Ôöé
Ôöé  2. TEAMSERVER SETUP (Day 1)                                     Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Install dependencies on Ubuntu VPS                       Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Clone and build Havoc from source                        Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Create teamserver profile (havoc.yaotl)                  Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Configure operator credentials                       Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Define listeners (HTTPS, SMB)                        Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Set Demon agent parameters                           Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ Configure malleable traffic profiles                 Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Harden teamserver (iptables, fail2ban)                   Ôöé
Ôöé     ÔööÔöÇÔöÇ Start teamserver with verbose logging                    Ôöé
Ôöé                                                                  Ôöé
Ôöé  3. REDIRECTOR CONFIGURATION (Day 1-2)                           Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Install Nginx on redirector VPS                          Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Configure SSL termination                                Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Set up reverse proxy rules                               Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Forward C2 URIs to teamserver                        Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ Redirect non-matching traffic to legit site          Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Configure access logging                                 Ôöé
Ôöé     ÔööÔöÇÔöÇ Test end-to-end connectivity                             Ôöé
Ôöé                                                                  Ôöé
Ôöé  4. PAYLOAD DEVELOPMENT (Day 2-3)                                Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Generate Demon shellcode via Havoc Client                Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Develop custom loader (C/Rust/Nim)                       Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ AES-encrypt shellcode                                Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Implement sleep obfuscation                          Ôöé
Ôöé     Ôöé   Ôö£ÔöÇÔöÇ Add sandbox checks                                   Ôöé
Ôöé     Ôöé   ÔööÔöÇÔöÇ Use indirect syscalls                                Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Test against AV/EDR in lab                               Ôöé
Ôöé     ÔööÔöÇÔöÇ Package for delivery vector                              Ôöé
Ôöé                                                                  Ôöé
Ôöé  5. OPERATIONAL TESTING (Day 3-4)                                Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Test beacon callback through full chain                  Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Verify redirector filtering                              Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Test sleep/jitter behavior                               Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Validate post-exploitation modules                       Ôöé
Ôöé     ÔööÔöÇÔöÇ Confirm kill switch functionality                        Ôöé
Ôöé                                                                  Ôöé
Ôöé  6. OPERATIONAL USE (Engagement period)                          Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Deploy payloads via approved vectors                     Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Manage sessions through Havoc Client                     Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Execute post-exploitation tasks                          Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Maintain operator logs                                   Ôöé
Ôöé     ÔööÔöÇÔöÇ Monitor infrastructure health                            Ôöé
Ôöé                                                                  Ôöé
Ôöé  7. TEAR-DOWN (Post-engagement)                                  Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Remove all implants from target systems                  Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Archive engagement logs                                  Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Destroy VPS instances                                    Ôöé
Ôöé     Ôö£ÔöÇÔöÇ Release domain names                                     Ôöé
Ôöé     ÔööÔöÇÔöÇ Provide IOCs to client for deconfliction                 Ôöé
Ôöé                                                                  Ôöé
ÔööÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÇÔöÿ
```

## Havoc Listener Configuration Decision Tree

```
Select Listener Type
Ôöé
Ôö£ÔöÇÔöÇ External (Internet-facing targets)?
Ôöé   Ôö£ÔöÇÔöÇ HTTPS Listener
Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Use valid SSL certificate
Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Configure malleable URIs
Ôöé   Ôöé   Ôö£ÔöÇÔöÇ Set User-Agent to match target
Ôöé   Ôöé   ÔööÔöÇÔöÇ Route through redirector
Ôöé   ÔööÔöÇÔöÇ HTTP Listener (lab only)
Ôöé       ÔööÔöÇÔöÇ Never use in production operations
Ôöé
Ôö£ÔöÇÔöÇ Internal (post-initial access)?
Ôöé   Ôö£ÔöÇÔöÇ SMB Listener (named pipe)
Ôöé   Ôöé   Ôö£ÔöÇÔöÇ For workstation-to-workstation pivoting
Ôöé   Ôöé   ÔööÔöÇÔöÇ No direct internet connectivity needed
Ôöé   ÔööÔöÇÔöÇ TCP Listener
Ôöé       ÔööÔöÇÔöÇ For direct internal connections
Ôöé
ÔööÔöÇÔöÇ Advanced?
    ÔööÔöÇÔöÇ External C2 Listener
        Ôö£ÔöÇÔöÇ Custom protocol over DNS
        Ôö£ÔöÇÔöÇ Domain fronting via CDN
        ÔööÔöÇÔöÇ Third-party service channels
```

## Terraform Deployment Template

```hcl
# main.tf - Automated Havoc C2 Infrastructure
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "teamserver" {
  ami           = "ami-0c7217cdde317cfec"  # Ubuntu 22.04
  instance_type = "t3.medium"
  key_name      = var.ssh_key_name

  vpc_security_group_ids = [aws_security_group.teamserver_sg.id]

  user_data = file("scripts/install_havoc.sh")

  tags = {
    Name = "havoc-teamserver"
  }
}

resource "aws_instance" "redirector" {
  ami           = "ami-0c7217cdde317cfec"
  instance_type = "t3.micro"
  key_name      = var.ssh_key_name

  vpc_security_group_ids = [aws_security_group.redirector_sg.id]

  user_data = file("scripts/install_redirector.sh")

  tags = {
    Name = "havoc-redirector"
  }
}

resource "aws_security_group" "teamserver_sg" {
  name = "havoc-teamserver-sg"

  ingress {
    from_port   = 40056
    to_port     = 40056
    protocol    = "tcp"
    cidr_blocks = [var.operator_ip]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [aws_instance.redirector.public_ip]
  }
}

resource "aws_security_group" "redirector_sg" {
  name = "havoc-redirector-sg"

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

## OPSEC Checklist

- [ ] Domains aged 30+ days before use
- [ ] Domains categorized in web proxies
- [ ] Valid SSL certificates installed
- [ ] Teamserver port (40056) firewalled to operator IPs only
- [ ] Redirector configured to filter non-C2 traffic
- [ ] Malleable C2 profile customized (URIs, headers, user-agent)
- [ ] Demon sleep set to 10+ seconds with 30%+ jitter
- [ ] Payload tested against target AV/EDR in lab
- [ ] Kill date set on all payloads
- [ ] Operator logs enabled and encrypted
- [ ] Emergency deconfliction process documented
