# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-print-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs graphics print
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for printing
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# converters
DEPENDS+=	pandoc-cli>=0:.././converters/pandoc-cli

# print
DEPENDS+=	a2ps>=0:../../print/a2ps
DEPENDS+=	ja-a2ps>=0:../../print/ja-a2ps
DEPENDS+=	enscript>=0:../../print/enscript
DEPENDS+=	ghostscript-agpl>=0:../../print/ghostscript-agpl
DEPENDS+=	gv>=0:../../print/gv
DEPENDS+=	okular>=0:../../print/okular
#DEPENDS+=	pdfjam>=0:../../print/pdfjam
DEPENDS+=	qpdf>=0:../../print/qpdf
DEPENDS+=	xpdf>=0:../../print/xpdf4

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
