# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-astronomy-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for astronomy
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

DEPENDS+=	${PYPKGPREFIX}-astropy>=6.0.0:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-astroquery>=0.4.7:../../pkgsrc_myownpkgs/py-astroquery
DEPENDS+=	${PYPKGPREFIX}-photutils>=1.11.0:../../pkgsrc_myownpkgs/py-photutils
DEPENDS+=	${PYPKGPREFIX}-ginga>=5.0.0:../../pkgsrc_myownpkgs/py-ginga

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"