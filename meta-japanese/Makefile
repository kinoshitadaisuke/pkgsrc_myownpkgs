# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-basictools-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs shells graphics math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for basic tools
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# input method
DEPENDS+=	mozc-elisp>=0:../../inputmethod/mozc-elisp
DEPENDS+=	mozc-server>=0:../../inputmethod/mozc-server
DEPENDS+=	mozc-tool>=0:../../inputmethod/mozc-tool

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
