# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-nvmm-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs emulator net
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for NVMM
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# input method
DEPENDS+=	qemu>=0:../../emulators/qemu
DEPENDS+=	tigervnc>=0:../../net/tigervnc

.include "../../mk/bsd.pkg.mk"
