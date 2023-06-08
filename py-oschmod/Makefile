# $NetBSD$

DISTNAME=	oschmod-0.3.12
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=o/oschmod/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/oschmod/
COMMENT=	Windows and Linux compatible chmod
LICENSE=	apache-2.0

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-flake8>=0:../../devel/py-flake8

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
