# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-net-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs net
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for network related software
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# net
DEPENDS+=	krdc>=0:../../net/krdc
DEPENDS+=	krfb>=0:../../net/krfb
DEPENDS+=	openntpd>=0:../../net/openntpd
DEPENDS+=	openvpn>=0:../../net/openvpn
DEPENDS+=	rsync>=0:../../net/rsync
DEPENDS+=	tigervnc>=0:../../net/tigervnc
DEPENDS+=	wget>=0:../../net/wget
DEPENDS+=	wget2>=0:../../net/wget2
#DEPENDS+=	yt-dlp>=0:../../net/yt-dlp

# security
DEPENDS+=	openssh>=0:../../security/openssh
DEPENDS+=	openssl>=0:../../security/openssl

# sysutils
DEPENDS+=	spice-gtk>=:../../sysutils/spice-gtk

# www
DEPENDS+=	curl>=0:../../www/curl

# pkgsrc_myownpkgs
#DEPENDS+=	yt-dlp>=0:../../pkgsrc_myownpkgs/yt-dlp

.include "../../mk/bsd.pkg.mk"
