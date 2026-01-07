# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-vpn-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs net
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for VPN related software
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# archivers
DEPENDS+=	zip>=0:../../archivers/zip

# converters
DEPENDS+=	base64>=0:../../converters/base64

# graphics
DEPENDS+=	ImageMagick>=0:../../graphics/ImageMagick

# lang
#DEPENDS+=	perl>=0:../../lang/perl5
#DEPENDS+=	python313>=0:../../lang/python313

# multimedia
#DEPENDS+=	ffmpeg6>=0:../../multimedia/ffmpeg6
#DEPENDS+=	ffmpeg7>=0:../../multimedia/ffmpeg7
DEPENDS+=	ffmpeg8>=0:../../multimedia/ffmpeg8

# net
DEPENDS+=	openvpn>=0:../../net/openvpn

# print
DEPENDS+=	ghostscript-agpl>=0:../../print/ghostscript-agpl

# sysutils
DEPENDS+=	coreutils>=0:../../sysutils/coreutils

# www
DEPENDS+=	curl>=0:../../www/curl

.include "../../mk/bsd.pkg.mk"
