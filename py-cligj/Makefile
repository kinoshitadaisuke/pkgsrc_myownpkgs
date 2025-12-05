# $NetBSD$

DISTNAME=	cligj-0.7.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	pkgsrc_myownpkgs python
MASTER_SITES=	${MASTER_SITE_PYPI:=c/cligj/}

MAINTAINER=	INSERT_YOUR_MAIL_ADDRESS_HERE # or use pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/mapbox/cligj
COMMENT=	Click params for commmand line interfaces to GeoJSON
#LICENSE=	BSD # TODO: from setup.py; needs to be adjusted

DEPENDS+=	${PYPKGPREFIX}-click>=4.0:../../devel/py-click

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-click>=0:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-test-cov>=0:../../devel/py-test-cov

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
